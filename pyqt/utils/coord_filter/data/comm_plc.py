from pycomm3 import LogixDriver
from typing import List

IP_ADDRESS = '192.168.1.10'


def write_tags(tag_name, tag_value):
    with LogixDriver(IP_ADDRESS) as plc:
        plc.write((tag_name, tag_value))


def read_tags(tag_name: str):
    """
        Read a tag from PLC and returns the value of it
        If it goes wrong, prints and returns the error

        Params:
            tag_name = tag to be read
        """
    try:
        with LogixDriver(IP_ADDRESS) as plc:
            return plc.read(tag_name).value
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e


def read_multiple(tag_list: List):
    with LogixDriver(IP_ADDRESS) as plc:
        tags = tag_list
        return plc.read(*tags)
