from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RestaRequest(_message.Message):
    __slots__ = ("numero3", "numero4")
    NUMERO3_FIELD_NUMBER: _ClassVar[int]
    NUMERO4_FIELD_NUMBER: _ClassVar[int]
    numero3: int
    numero4: int
    def __init__(self, numero3: _Optional[int] = ..., numero4: _Optional[int] = ...) -> None: ...

class RestaResponse(_message.Message):
    __slots__ = ("resultado",)
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    resultado: int
    def __init__(self, resultado: _Optional[int] = ...) -> None: ...
