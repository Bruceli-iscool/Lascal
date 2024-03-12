# collection of functions

def variables(line, dict):
    """Store variables"""
    line = line.replace(" ", "")
    name, value = line.split("=")
    dict[name] = value
def input_statement():
    pass