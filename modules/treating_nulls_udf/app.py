import sys

def treating_nulls(value, flag: int):
    if flag == 1:
        return value if value is not None else 0
    elif flag == 0:
        return "Not Available" if value in (None, '') else value
    elif flag == 2:
        return (str(value[:-2]) + ":" + str(value[-2:]))
    else:
        return value