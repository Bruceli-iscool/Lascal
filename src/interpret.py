import process
import stdlib

mode = 0
var = {}

def interpret(line):
    # set as global variable
    global mode
    line = line.lstrip()
    if  mode != 1:
        if line.startswith("start"):
            mode = 1
        elif line.startswith("//"):
            return
        elif "=" in line:
            stdlib.variables(line, var)
        elif len(line) < 1 or line == " ":
            return
        else:
            print(f"Lascal: Syntax Error: Statements outside main at [{line}].")
            return
    else:
        if line.startswith("end."):
            mode = 0
        elif len(line) < 1 or line == " ":
            return
        else:
            process.process(line, var, 1)
            

