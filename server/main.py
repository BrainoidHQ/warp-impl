import sys
from typing import Callable, Dict, Optional
from asyncio import StreamReader, StreamWriter, get_event_loop
from aioquic.asyncio import QuicConnectionProtocol, serve
from aioquic.h3.connection import H3_ALPN, H3Connection
from aioquic.h3.events import H3Event, HeadersReceived, WebTransportStreamDataReceived, DatagramReceived
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.connection import stream_is_unidirectional
from aioquic.quic.events import ProtocolNegotiated, StreamReset, QuicEvent, ConnectionTerminated, StreamDataReceived

QuicStreamHandler = Callable[[StreamReader, StreamWriter], None]

class WT(QuicConnectionProtocol):
  def __init__(self, quic: H3Connection, stream_handler: Optional[QuicStreamHandler] = None):
    self._http: Optional[H3Connection] = None
    self._handler: Optional[QuicStreamHandler] = None
    super().__init__(quic, stream_handler)
  def quic_event_received(self, event: QuicEvent) -> None:
    print(event)
    if isinstance(event, ProtocolNegotiated):
      print("ALPN negotiation completed")
      self._http = H3Connection(self._quic, enable_webtransport = True)

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
