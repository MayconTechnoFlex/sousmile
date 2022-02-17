"""Types for the application"""

from typing import Literal, Callable, Union, TypedDict

# Literals
TagTypes = Literal["string", "int", "float", ""]
ActionsToConfirm = Literal["MoveHome", ""]
UsersName = Literal["oper", "eng", "rn", ""]

# Unions
PLCReturn = Union[str, int, float, list, dict, Exception]

# Functions
AltValShowDialog_WithText = Callable[[str, str, TagTypes], None]
AltValShowDialog_WithoutText = Callable[[str, TagTypes], None]

# Dicts
class AlarmDict(TypedDict):
    """
    Type for alarms

    id: int
    time: str
    message: str
    """
    id: int
    time: str
    message: str

class UsersAccounts(TypedDict):
    """
    Type for users accounts

    oper: str
    eng: str
    rn: str
    """
    oper: str
    eng: str
    rn: str

# todo => criar tipagem para as informações recebidas do CLP?
