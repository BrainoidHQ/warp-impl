#https://datatracker.ietf.org/doc/draft-lcurley-warp/

from typing import TypedDict, List

class WarpMessage(TypedDict):
  message_type: int
  message_length: int
  payload: any

# A SETUP message is the first message that is exchanged by the client and the server;
# it allows the peers to establish the mutually supported version and agree on the initial configuration.
# It is a sequence of key-value pairs called _SETUP parameters_
class SETUPParameter(TypedDict):
  key: int
  value_length: int
  value: int

class ClientSETUP(TypedDict):
  num_of_supported_versions: int
  supported_versions: List[int]
  parameters: List[SETUPParameter] # ROLE(0x00) parameter is required

class ServerSETUP(TypedDict):
  selected_version: int
  parameters: List[SETUPParameter]

# A OBJECT message contains a single media object associated with a
# specified track, as well as associated metadata required to deliver,
# cache, and forward it.
class OBJECT(TypedDict):
  broadcast_uri: str
  track_id: int
  object_id: int
  delivery_order: int
  payload: any

class TrackDescriptor(TypedDict):
  track_id: int
  container_format: int
  container_init_payload: any

# The sender advertises an available broadcast and its tracks via a
# CATALOG message.
class CATALOG(TypedDict):
  broadcast_uri: str
  track_count: int
  track_descriptors: List[TrackDescriptor]

#After receiving a CATALOG message (Section 6.3, the receiver sends a
# SUBSCRIBE message to indicate that it wishes to receive the indicated
# tracks within a broadcast.
class SUBSCRIBE(TypedDict):
  broadcast_uri: str
  track_count: str
  track_ids: List[int]
