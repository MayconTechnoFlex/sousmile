"""Tipagem para a Aplicação"""
#######################################################################################################
# Importações
#######################################################################################################
from typing import Literal, Union, TypedDict
#######################################################################################################
# Literals
#######################################################################################################
TagTypes = Literal["string", "int", "float", ""]
ActionsToConfirm = Literal["MoveHome", "CheckUTOOL", "ChangeTool", ""]
#######################################################################################################
# Unions
#######################################################################################################
PLCReturn = Union[str, int, float, list, dict, Exception]
#######################################################################################################
# Dicts
#######################################################################################################
class AlarmDict(TypedDict):
    """
    Tipagem para alarmes

    id: int
    time: str
    message: str
    """
    id: int
    time: str
    message: str
#######################################################################################################
