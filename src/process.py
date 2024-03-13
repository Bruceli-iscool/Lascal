import stdlib

def process(line, dict):
    if ";" in line:
        line = line.replace(';', "")
    if line.startswith("println "):
        line = line.replace("println ", "")
        print(line)
    elif line.startswith("//"):
        return
    elif "=" in line:
        stdlib.variables(line, dict)
    elif line.startswith("inputln"):
        stdlib.input_statement(line)
    else:
        print("Lascal: Syntax Error: Unexpected identifier.")
