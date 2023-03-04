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
    print(event)
    if isinstance(event, DatagramReceived):
      print("Datagram: {}".format(event.data.decode(encoding = "utf-8")))
      self._http.send_datagram(self._session_id, event.data)
      self._http._quic.send_datagram_frame(event.data)
    elif isinstance(event, WebTransportStreamDataReceived):
      print("Stream Data Received")
      if not event.stream_ended:
        return
      if stream_is_unidirectional(event.stream_id):
        print("Undirectional Stream: {}".format(event.data.decode("utf-8")))
        # Create counter stream with the same session id
        res = self._http.create_webtransport_stream(event.session_id, is_unidirectional = True)
      else:
        print("Bidirectional Stream: {}".format(event.data.decode("utf-8")))
        # Create new stream with the same stream id (its session id is gonna be different)
        res = event.stream_id
      self._http._quic.send_stream_data(res, event.data, end_stream = True)
      self.stream_closed(event.session_id)


