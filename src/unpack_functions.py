import interpret


def unpack(func, dict, vars):
    action = dict[func]
    action = action[0:]
    line = action.split(":")
    for x in line:
        interpret.interpret(x)
def unpackF(func, dict, vars):
    action = dict[func]
    action = action[0:]
    line = action.split(":")
    for x in line:
            if x.startswith("return"):
                x = x.replace(";", "")
                x = x.lstrip()
                value = x.replace("return ", "")
                return value
            else:
                interpret.interpret(x)
