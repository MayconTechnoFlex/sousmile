"""Control of the PLC Read and Write functions"""

from pycomm3 import LogixDriver
from typing import Union
from utils.Types import PLCReturn

from utils.alarm_control import alarm_tag_list, get_alarm_message
from screens.in_out import tags_input, tags_output, tags_module

IP = '192.168.1.10'


def read_tags(tag_name: str) -> PLCReturn:
    """
    Read a tag from PLC and returns the value of it
    If it goes wrong, print's the error
    """
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_name).value
    except Exception as e:
        print(f"{e} - Error on plc communication")
        return e

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

def read_multiples(tag_list: list[str]):
    try:
        with LogixDriver(IP) as plc:
            return plc.read(*tag_list)
    except Exception as e:
        print(f"{e} - Error on plc communication")

### testing alarm reading from PLC
alarmProcess = read_multiples(alarm_tag_list)
input = read_multiples(tags_input)
output = read_multiples(tags_output)
module = read_multiples(tags_module)
for i in range(0, 96):
    if alarmProcess[i][1]:
        message = get_alarm_message(i)
        print(message)

for i in range(0, 16):
    if i <= 7:
        print(module[i])
    print(input[i])
    print(output[i])
