from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class calculoRequest(_message.Message):
    __slots__ = ("numero1", "numero2", "numero3", "numero4")
    NUMERO1_FIELD_NUMBER: _ClassVar[int]
    NUMERO2_FIELD_NUMBER: _ClassVar[int]
    NUMERO3_FIELD_NUMBER: _ClassVar[int]
    NUMERO4_FIELD_NUMBER: _ClassVar[int]
    numero1: int
    numero2: int
    numero3: int
    numero4: int
    def __init__(self, numero1: _Optional[int] = ..., numero2: _Optional[int] = ..., numero3: _Optional[int] = ..., numero4: _Optional[int] = ...) -> None: ...

class calculoResponse(_message.Message):
    __slots__ = ("resultado",)
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    resultado: int
    def __init__(self, resultado: _Optional[int] = ...) -> None: ...
