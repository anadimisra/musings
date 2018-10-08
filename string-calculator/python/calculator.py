import re
def Add(input):
    inp_array = re.split('[\n,]+',input)
    result = 0
    for inp in inp_array:
        if int(inp) <= 1000:
            result += int(inp)
    return result

