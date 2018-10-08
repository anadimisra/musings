def Add(input):
    inp_array = input.split("\n")
    result = 0
    for inp in inp_array:
        result += int(inp)
    return result

