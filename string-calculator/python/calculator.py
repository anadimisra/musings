import re
def Add(input):
    inp_array = re.split('[\n,]+',input)
    result = 0
    for inp in inp_array:
        if get_int(inp) <= 1000:
            result += get_int(inp)
    return result

def get_int(str):
    s = str.strip()
    return int(s) if s else 0

class NegativeNumberException(Exception):
    pass
