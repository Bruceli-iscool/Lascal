import stdlib

def process(line, dict, mode, funcDict):
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
        return stdlib.input_statement(line, dict)
    elif mode == 1:
        print(f"Lascal: Syntax Error: Unexpected identifier at [{original_line}].")
        return
    elif mode == 2:
        return line
