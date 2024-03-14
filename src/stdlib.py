import process
# Standard Libary

def stdlibStatements(line, dict):
    cb = process.process(line, dict, 2)
    return cb
def variables(line, dict):
    """Store variables"""
    line = line.replace(" ", "")
    line = line.replace('\\s+', " ")
    name, value = line.split("=")
    value = stdlibStatements(value, dict)
    dict[name] = value
def input_statement(line, dict):
    """Accept Input"""
    line = line.replace("inputln ", "")
    if "'" in line:
        line = line.replace("'", "")
    elif '"' in line:
        line =line.replace('"', "")
    for key, value in dict.items():
        line = line.replace(str(key), str(value))
    value = input(line)
    if type(value) == str:
        value = "'" + value + "'"
    return value


        
    