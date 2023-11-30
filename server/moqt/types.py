from typing import TypedDict, List, Optional, Union

class Parameter(TypedDict):
    ParameterType: int
    ParameterLength: int
    ParameterValue: Union[int, str, bytes]

class Location(TypedDict):
    Mode: int
    Value: Optional[int]

class SubscribeRequest(TypedDict):
    FullTrackNameLength: int
    FullTrackName: str
    StartGroup: Location
    StartObject: Location
    EndGroup: Location
    EndObject: Location
    TrackRequestParameters: List[Parameter]

class SubscribeOk(TypedDict):
    TrackNamespace: str
    TrackName: str
    TrackID: int
    Expires: int

class SubscribeError(TypedDict):
    TrackNamespace: str
    TrackName: str
    ErrorCode: int
    ReasonPhraseLength: int
    ReasonPhrase: str

class Unsubscribe(TypedDict):
    TrackNamespace: str
    TrackName: str

class SubscribeFin(TypedDict):
    TrackNamespace: str
    TrackName: str
    FinalGroup: int
    FinalObject: int

class SubscribeRst(TypedDict):
    TrackNamespace: str
    TrackName: str
    ErrorCode: int
    ReasonPhraseLength: int
    ReasonPhrase: str
    FinalGroup: int
    FinalObject: int

class Announce(TypedDict):
    TrackNamespace: str
    NumberOfParameters: int
    Parameters: List[Parameter]

class AnnounceOk(TypedDict):
    TrackNamespace: str

class AnnounceError(TypedDict):
    TrackNamespace: str
    ErrorCode: int
    ReasonPhraseLength: int
    ReasonPhrase: str

class Unannounce(TypedDict):
    TrackNamespace: str

class Goaway(TypedDict):
    NewSessionURI: str

class ObjectMessage(TypedDict, total=False):
    TrackID: int
    GroupSequence: int
    ObjectSequence: int
    ObjectSendOrder: int
    ObjectPayloadLength: int  # Optional
    ObjectPayload: bytes

