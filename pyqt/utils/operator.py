OPERATOR_NAME = ''
OPERATOR_ID = ''


def set_operator(name: str, id: str) -> None:
    global OPERATOR_NAME, OPERATOR_ID
    OPERATOR_NAME = name
    OPERATOR_ID = id


def get_operator_name() -> str:
    global OPERATOR_NAME
    if OPERATOR_NAME != '':
        return OPERATOR_NAME
    else:
        return "Sem operador"


def get_operator_id() -> str:
    global OPERATOR_ID
    return OPERATOR_ID
