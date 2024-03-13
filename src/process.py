import stdlib

def process(line, dict):
    if ";" in line:
        line = line.replace(';', "")
    if line.startswith("println "):
        line = line.replace("println ", "")
        for key, value in dict.items():
            line = line.replace(str(key, value))
        print(line)
    elif line.startswith("//"):
        return
    elif "=" in line:
        stdlib.variables(line, dict)
    elif line.startswith("inputln"):
        stdlib.input_statement(line, dict)
    else:
        print(f"Lascal: Syntax Error: Unexpected identifier at [{line}].")
        return
