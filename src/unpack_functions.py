import process


def unpack(func, dict, vars):
    action = dict[func]
    action = action[0:]
    for char in action:
        if char == ":":
            line = action.split(":")
            for x in line:
                process.process(x, vars, 2)
def unpackF(func, dict, vars):
    action = dict[func]
    action = action[0:]
    for char in action:
        if char == ":":
            line = action.split(":")
            for x in line:
                if x.startswith("return"):
                    x = x.replace(";", "")
                    value = x.replace("return ", "")
                    return value
                else:
                    process.process(x, vars, 2)
