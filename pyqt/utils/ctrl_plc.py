from pycomm3 import LogixDriver
from typing import Union

IP = '192.168.1.10'


def read_tags(tag_name: str) -> Union[str, int, float, list, dict]:
    """
    Read a tag from PLC and returns the value of it
    If it goes wrong, print's the error
    """
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_name).value
    except Exception as e:
        print(f"{e} - Error on plc communication")

def write_tag(tag_name: str, value: Union[str, int, float]):
    """
    Write a tag on PLC
    If it goes wrong, print's the error
    """
    try:
        with LogixDriver(IP) as plc:
            plc.write((tag_name, value))
    except Exception as e:
        print(f"{e} - Error on plc communication")

def read_multiples(tag_list):
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_list)
    except Exception as e:
        print(f"{e} - Error on plc communication")
