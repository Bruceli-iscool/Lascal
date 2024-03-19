import stdlib
import unpack_functions

prod = {}
type = 0
statement = 0

def process(line, dict, mode, funcDict):
    global type, statement, prod
    if type == 0:
        original_line = line
        if ";" in line:
            line = line.replace(';', "")
        if line.startswith("println "):
            line = line.replace("println ", "")
            
            for key, value in dict.items():
                line = line.replace(str(key), str(value))
            try:
                line = eval(line)
            except Exception:
                if '"' in line:
                    line =line.replace('"', "")
                elif "'" in line:
                    line = line.replace("'", "")
            finally:
                print(line)
        elif line.startswith("//"):
            return
        elif "=" in line and "==" not in line and "!=" not in line:
            stdlib.variables(line, dict, funcDict)
        elif line.startswith("inputln"):
            line = line.replace("inputln", "")
            stdlib.input_statement(line, dict)
        elif line.startswith("if"):
            line = line.replace("if (", "")
            line = line.replace(")", "")
            line = line.replace("{", "")
            for key, value in dict.items():
                line = line.replace(str(key), str(value))
            global statement
            statement = line
            prod[statement] = ""
            type = 1
        elif mode == 1:
            print(f"Lascal: Syntax Error: Unexpected identifier at [{original_line}].")
            return
        elif mode == 2:
            return line
    elif type == 1:
        if line.startswith("}"):
            if statement:
                unpack_functions.unpack(statement, prod, dict)
                prod[statement] = ""
                type = 0
            else:
                return
        elif line == statement:
            return
        else:
            prod[statement] = prod[statement] + ':' + line
    
