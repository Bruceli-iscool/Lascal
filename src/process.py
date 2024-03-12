def process(line):
    if ";" in line:
        line = line.replace(';', "")
    if line.startswith("println "):
        line = line.replace("println ", "")
        print(line)
    elif line.startswith("//"):
        return
    else:
        print("Lascal: Syntax Error: Unexpected identifier.")
