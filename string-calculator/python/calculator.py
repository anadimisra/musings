import re
def Add(input):
    inp_array = parse_delim(input)
    result = 0
    for inp in inp_array:
        if get_int(inp) <= 1000:
            result += get_int(inp)
    return result

def get_int(str):
    s = str.strip()
    return int(s) if s else 0

# Parse Delim and Split String
def parse_delim(str):
    delims_raw = re.search(r'(?<=//)(.*)(?=\n)', str)
    if delims_raw:
        print delims_raw.group(0)
        delim = delims_raw.group(0)
        return re.split(delim,str)
    else:
        return re.split('[\n,]+',str)
    
class NegativeNumberException(Exception):
    pass
