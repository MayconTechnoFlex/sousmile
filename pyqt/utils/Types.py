"""Types for the application"""

from typing import Literal, Union, TypedDict

# Literals
TagTypes = Literal["string", "int", "float", ""]
ActionsToConfirm = Literal["MoveHome", "CheckUTOOL", "ChangeTool", ""]

# Unions
PLCReturn = Union[str, int, float, list, dict, Exception]

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

# todo => criar tipagem para as informações recebidas do CLP?
