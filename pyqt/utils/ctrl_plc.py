from pycomm3 import LogixDriver

IP = '192.168.1.10'


def read_tags(tag_name):
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_name).value
    except Exception(e):
        print(f"{e} - Error on plc communication")

def write_tag(tag_name, value):
    try:
        with LogixDriver(IP) as plc:
            plc.write((tag_name, value))
    except Exception(e):
        print(f"{e} - Error on plc communication")

def read_multiples(tag_list):
    try:
        with LogixDriver(IP) as plc:
            return plc.read(tag_list)
    except Exception(e):
        print(f"{e} - Error on plc communication")