import process
# Standard Libary

def stdlibStatements(line):
    cb = process.process(line)
    return cb
def variables(line, dict):
    """Store variables"""
    line = line.replace(" ", "")
    line = line.replace('\s+', " ")
    name, value = line.split("=")
    value = stdlibStatements(value)
    dict[name] = value
def input_statement(line):
    """Accept Input"""
    line = line.replace("inputln ", "")
    if "'" in line:
        line = line.replace("'", "")
    elif '"' in line:
        line =line.replace('"', "")
    value = input(line)
    if type(value) == str:
        value = "'" + value + "'"
    return value
        
    