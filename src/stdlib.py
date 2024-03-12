# collection of functions

def variables(line, dict):
    """Store variables"""
    if " = " in line:
        name, value = line.split(" = ")
    elif "=" in line:
        name, value = line.split("=")
    elif " =" in line:
        name, value = line.split(" =")
    elif "= " in line:
        name, value = line.split("= ")
    dict[name] = value
def input_statement(line):
    pass