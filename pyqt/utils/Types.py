from typing import Literal, Callable

TagTypes = Literal["string", "int", "float", ""]
ActionsToConfirm = Literal["MoveHome", ""]
AltValShowDialog_WithText = Callable[[str, str, TagTypes], None]
AltValShowDialog_WithoutText = Callable[[str, TagTypes], None]
