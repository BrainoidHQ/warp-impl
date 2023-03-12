from collections import defaultdict
from aioquic.h3.connection import H3Connection
from aioquic.h3.events import H3Event, DatagramReceived, WebTransportStreamDataReceived
from aioquic.quic.connection import stream_is_unidirectional

class ConnectionHandler:
  def __init__(self, session_id, http: H3Connection) -> None:
    self._session_id = session_id
    self._http = http
    self._texts = defaultdict(bytes)
  def stream_closed(self, stream_id: int) -> None:
    try:
      del self._texts[stream_id]
    except KeyError:
      print("Cannot delete {}".format(stream_id))
      pass
  def event_received(self, event: H3Event) -> None:
    if isinstance(event, DatagramReceived):
      print("Datagram: {}".format(event.data.decode(encoding = "utf-8")))
      self._http.send_datagram(self._session_id, event.data)
    elif isinstance(event, WebTransportStreamDataReceived):
      self._texts[event.stream_id] += event.data
      # if event.stream_id not in self._texts:
      #   print("Stream has ended but no payload has been found. Terminating")
      #   return
      payload = self._texts[event.stream_id]
      if stream_is_unidirectional(event.stream_id):
        self.unidirectional_stream_received(event, payload)
      else:
        self.bidirectional_stream_received(event, payload)
  def unidirectional_stream_received(self, event, payload) -> None:
    print("Undirectional Stream: {}".format(payload.decode("utf-8")))
    res = self._http.create_webtransport_stream(event.session_id, is_unidirectional = True)
    self._http._quic.send_stream_data(res, payload, end_stream = True)
    self.stream_closed(event.stream_id) #Delete corresponding payload (temporarily for echo server)
  def bidirectional_stream_received(self, event, payload) -> None:
    print("Bidirectional Stream: {}".format(payload.decode("utf-8")))
    res = event.stream_id
    self._http._quic.send_stream_data(res, payload, end_stream = False)
