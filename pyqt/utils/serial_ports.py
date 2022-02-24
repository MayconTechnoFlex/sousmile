import serial

PORT = ""

def get_serial_ports() -> list[str]:
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except Exception:
            pass
    return result

def set_my_port(port: str):
    """
    Set's the port in the module variable

    Params:
        port = the port string
    """
    global PORT
    PORT = port

def get_my_port() -> str:
    """
    Returns the port from the module variable

    Return:
        the port string
    """
    global PORT
    return PORT


if len(get_serial_ports()) == 1:
    set_my_port(get_serial_ports()[0])

