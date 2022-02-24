"""Control of the PLC Read and Write functions"""

from pycomm3 import LogixDriver, Tag
from typing import Union, List
from utils.Types import PLCReturn


IP = '192.168.1.10'


def read_tags(tag_name: str) -> PLCReturn:
    """
    Read a tag from PLC and returns the value of it
    If it goes wrong, prints and returns the error

    Params:
        tag_name = tag to be read
    """
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_name).value
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e


def write_tag(tag_name: str, value: Union[str, int, float]) -> Union[None, Exception]:
    """
    Write a tag on PLC
    If it goes wrong, print's the error

    Params:
        tag_name = tag to be read
        value = what the function will write in the tag
    """
    try:
        with LogixDriver(IP) as plc:
            plc.write((tag_name, value))
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e


def read_multiples(tag_list: List[str]) -> Union[List[Tag], Exception]:
    """
    Read a tag from PLC and returns the value of it
    If it goes wrong, prints and returns the error

    Params:
        tag_list = list of tag to be read
    """
    try:
        with LogixDriver(IP) as plc:
            return plc.read(*tag_list)
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e
