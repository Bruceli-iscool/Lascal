import process


def unpack(func, dict, vars):
    action = dict[func]
    action = action[0:]
    for char in action:
        if char == ":":
            line = action.split(":")
            for x in line:
                process.process(x, vars, 2)
