from collections import defaultdict
from aioquic.h3.connection import H3Connection
from aioquic.h3.events import H3Event

class ConnectionHandler:
  def __init__(self, session_id, http: H3Connection) -> None:
    self._session_id = session_id
    self._http = http
    self._texts = defaultdict(bytes)


