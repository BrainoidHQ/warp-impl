import sys
from typing import Dict, Literal, Optional
from asyncio import get_event_loop
from aioquic.asyncio import QuicConnectionProtocol, serve
from aioquic.h3.connection import H3_ALPN, H3Connection
from aioquic.h3.events import H3Event, HeadersReceived, WebTransportStreamDataReceived, DatagramReceived
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import ProtocolNegotiated, StreamReset, QuicEvent, ConnectionTerminated, StreamDataReceived

from handler import ConnectionHandler

class WT(QuicConnectionProtocol):
  def __init__(self, *args, **kwargs):
    self._http: Optional[H3Connection] = None
    self._handler: Optional[ConnectionHandler] = None
    super().__init__(*args, **kwargs)
  def quic_event_received(self, event: QuicEvent) -> None:
    if isinstance(event, ProtocolNegotiated):
      self._http = H3Connection(self._quic, enable_webtransport = True)
    elif isinstance(event, StreamReset) and self._handler is not None:
      self._handler.stream_closed(event.stream_id)
      print("Stream closed due to RESETS")
    if self._http is None:
      return
    for h3_event in self._http.handle_event(event):
      if isinstance(h3_event, HeadersReceived):
        headers = {}
        for key, value in h3_event.headers:
          headers[key] = value
        self._handshake_wt(h3_event.stream_id, headers)
        return
      if self._handler:
        self._handler.event_received(h3_event)
  def _handshake_wt(self, stream_id: int, rh: Dict[bytes, bytes]) -> None:
    # Check if the event is WebTransport in the first place
    header_method = rh.get(b":method")
    header_protocol = rh.get(b":protocol")
    if (header_method != b"CONNECT") or (header_protocol != b"webtransport"):
      self._http.send_headers(stream_id, self._encode_header(400), True)
      return
    # Check if the header contains sufficient properties for WebTransport connection establishment
    header_authority = rh.get(b":authority")
    header_path = rh.get(b":path")
    if (header_path is None) or (header_authority is None):
      self._http.send_headers(stream_id, self._encode_header(400), True)
      return
    if header_path == b"/counter" and self._handler is None:
      self._handler = ConnectionHandler(stream_id, self._http)
      headers = self._encode_header(200)
      headers.append((b"sec-webtransport-http3-draft", b"draft02"))
      self._http.send_headers(stream_id, headers, False)
      return
    self._http.send_headers(stream_id, self._encode_header(404), True)
  def _encode_header(self, status_code: int) -> list[tuple[Literal, bytes]]:
    return [(b":status", str(status_code).encode())]

def setup(addr: str, port: str):
  if __name__ != "__main__":
    return
  config = QuicConfiguration(
    alpn_protocols = H3_ALPN,
    is_client = False,
    max_datagram_frame_size = 65536,
    connection_id_length = 8
  )
  config.load_cert_chain(sys.argv[1], sys.argv[2])
  loop = get_event_loop()
  loop.run_until_complete(
    serve(
      addr,
      port,
      configuration = config,
      create_protocol= WT,
    ))
  try:
    print("https://{}:{}".format(addr, port))
    loop.run_forever()
  except KeyboardInterrupt:
    pass

setup("0.0.0.0", "4433")
