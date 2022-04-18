def sub(
    _str:str,
    _from:int,
    _to:int=None
) -> str:
    _to = _from + 1 if _to == None else _to
    return _str[_from:_to]

def tostr(
    val,
    _hex:bool=False
) -> str:
    return str(val) if not _hex else str(hex(val))

def tonum(
    _str:str
) -> float or int:
    try:
        return int(_str)
    except ValueError:
        return float(_str)
