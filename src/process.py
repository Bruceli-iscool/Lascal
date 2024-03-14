import stdlib

def process(line, dict, mode=1):
    if ";" in line:
        line = line.replace(';', "")
    if line.startswith("println "):
        line = line.replace("println ", "")
        for key, value in dict.items():
            line = line.replace(str(key), str(value))
        if '"' in line:
            line =line.replace('"', "")
        elif "'" in line:
            line = line.replace("'", "")
        print(line)
    elif line.startswith("//"):
        return
    elif "=" in line:
        stdlib.variables(line, dict)
    elif line.startswith("inputln"):
        stdlib.input_statement(line, dict)
    elif mode == 1:
        print(f"Lascal: Syntax Error: Unexpected identifier at [{line}].")
        return
    elif mode == 2:
        return line
