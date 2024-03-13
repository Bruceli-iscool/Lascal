import process
import stdlib

mode = 0
var = {}
procedures = {}

def interpret(line):
    # set as global variable
    global mode
    line = line.lstrip()
    if  mode != 1:
        if line.startswith("start"):
            mode = 1
        elif line.startswith("//"):
            return
        elif line.startswith("procedure "):
            mode = 2
            line = line.replace("{", "")
            name = line.replace(" ", "")
        elif "=" in line:
            stdlib.variables(line, var)
        elif len(line) < 1 or line == " ":
            return
        else:
            print(f"Lascal: Syntax Error: Statements outside main at [{line}].")
            return
    elif mode == 1:
        if line.startswith("end."):
            mode = 0
        elif len(line) < 1 or line == " ":
            return
        else:
            process.process(line, var, 1)
    elif mode == 2:
        if line.replace(" ", "") == name:
            pass
        elif line.startswith("}"):
            mode = 0
        else:
            procedures[name] = ':' + line

