import process

def unpack(func, dict):
    action = dict[func]
    action = action[0:]
    for x in ":" in action:
        line = action.split(":")
        process.process(line)
        