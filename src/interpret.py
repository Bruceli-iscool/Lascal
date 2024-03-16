import process
import stdlib
import unpack_functions
name = 0
mode = 0
var = {}
func = {}
procedures = {}

def interpret(line):
    # set as global variable
    original_line = line
    global mode
    line = line.lstrip()
    if line.startswith("/*"):
        mode = 4
        return
    if  mode ==0:
        if line.startswith("start"):
            mode = 1
        elif line.startswith("//"):
            return
        elif line.startswith("procedure "):
            global name
            line = line.replace("procedure ", "")
            line = line.replace("{", "")
            name = line.replace(" ", "")
            mode = 2
        elif line.startswith("func"):
            line =line.replace("func ", "")
            line = line.replace("{", "")
            name = line.replace(" ", "")
            mode = 3
        elif "=" in line:
            stdlib.variables(line, var, func)
        elif len(line) < 1 or line == " ":
            return
        else:
            print(f"Lascal: Syntax Error: Statements outside main at [{original_line}].")
            return
    elif mode == 1:
        line = line.replace(";", "")
        if line.startswith("end."):
            mode = 0
        elif len(line) < 1 or line == " ":
            return
        elif line.replace(" ", "") in procedures:
            line = line.replace(";", "")
            line = line.replace(" ", "")
            unpack_functions.unpack(line, procedures, var)
        elif line.replace(" ", "") in func:
            line = line.replace(";", "")
            line = line.replace(" ", "")
            unpack_functions.unpackF(line, func, var)
        elif line.startswith("if"):
            line = line.replace("if (", "")
            line = line.replace(")", "")
            line = line.replace("{", "")
            mode = 5

        else:
            process.process(line, var, 1, func)
    elif mode == 2:
        if line.replace(" ", "") == name:
            return
        elif line.startswith("}"):
            mode = 0
        else:
            procedures[name] = ':' + line
    elif mode == 3:
        if line.replace(" ", "") == name:
            return
        elif line.startswith("}"):
            mode = 0
        else:
            func[name] = ':' + line
    elif mode == 4:
        if "*/" in line:
            mode = 0
        elif '*/' not in line:
            return
        

