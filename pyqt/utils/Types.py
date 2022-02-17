"""Types for the application"""

from typing import Literal, Callable, Union

TagTypes = Literal["string", "int", "float", ""]
ActionsToConfirm = Literal["MoveHome", ""]
UsersName = Literal["oper", "eng", "rn", ""]
AltValShowDialog_WithText = Callable[[str, str, TagTypes], None]
AltValShowDialog_WithoutText = Callable[[str, TagTypes], None]
