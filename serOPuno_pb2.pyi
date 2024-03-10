from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SumarRequest(_message.Message):
    __slots__ = ("numero1", "numero2")
    NUMERO1_FIELD_NUMBER: _ClassVar[int]
    NUMERO2_FIELD_NUMBER: _ClassVar[int]
    numero1: int
    numero2: int
    def __init__(self, numero1: _Optional[int] = ..., numero2: _Optional[int] = ...) -> None: ...

class SumaResponse(_message.Message):
    __slots__ = ("resultado",)
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    resultado: int
    def __init__(self, resultado: _Optional[int] = ...) -> None: ...
