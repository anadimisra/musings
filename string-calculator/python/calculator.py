import re
def Add(input):
    inp_array = re.split('[\n,]+',input)
    result = 0
    for inp in inp_array:
        result += int(inp)
    return result

