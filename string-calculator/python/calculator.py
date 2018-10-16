import re
from numpy import size
def Add(input):

    # if input has delims specified,
    # split delims from input and retrieve input array
    if '//' in input:
        split_delim_and_input = input.split('\n',1)
        inp_array = parse_delim(split_delim_and_input)
    else:
        inp_array = parse_delim(input)

    print "input array: " + ",".join(inp_array)

    # loop through input array and calculate result.
    result = 0
    for inp in inp_array:
        if get_int(inp) <= 1000:
            result += get_int(inp)
    return result

# returns int from str.
# returns 0 for empty inputs.
# returns 0 for non-int inputs.
def get_int(str):
    s = str.strip()
    if s:
        try:
            if int(s) < 0:
                raise NegativeNumberException('negative numbers are not allowed')
            else:
                return int(s) 
        except ValueError:
            return 0
    else:
        return 0


# Parse Single or Multiple Delims and Splits String using Delims.
# Allows Delims to be specified as //[%][-]\n or //;\n
# If no delims were found, parses by \n and , delims.

def parse_delim(inp):
    split_inputs = []
    if size(inp) == 1:
        # parse with default delims.
        split_inputs = re.split(r'[\n,]+',inp)
    else:
    
        symbols = '!@#$%^&*-;'
        delims_mult = re.findall(r'(?<=\[)[' + symbols + ']+(?=\])',inp[0])

        # try parsing with multiple delim pattern.
        if delims_mult:
            delims = "[" + "".join(delims_mult) + ']+'
            print 'delims: ' + delims
            split_inputs = re.split(delims,inp[1])
        
        else:
            # try parsing with single delim pattern.
            delims_single = re.findall(r'(?<=//)[' + symbols + ']+',inp[0])
            if delims_single:
                delims = "[" + "".join(delims_single) + ']+'
                print "delims: " + delims
                split_inputs = re.split(delims,inp[1])

    print "inputs: " + ",".join(split_inputs)
    return split_inputs        

   
class NegativeNumberException(Exception):
    pass
