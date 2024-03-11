import process

mode = 0

def interpret(line):
    # set as global variable
    global mode
    line = line.lstrip()
    if  mode != 1:
        if line.startswith("start"):
            mode = 1
        elif line.startswith("//"):
            return
        else:
            print("Liscal: Syntax Error: Statements outside main.")
    else:
        if line.startswith("end."):
            mode = 0
        elif line.startswith("//"):
            return
        else:
            process.process(line)
interpret("start")
interpret("println 1;")
interpret("end.")