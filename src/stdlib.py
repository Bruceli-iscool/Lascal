import process
import unpack_functions
# Standard Libary

def stdlibStatements(line, dict, funcdict):
    cb = process.process(line, dict, 2, funcdict)
    return cb
def variables(line, dict, funcdict):
    """Store variables"""
    line = line.replace(" ", "")
    line = line.replace('\\s+', " ")
    name, value = line.split("=")
    if value.replace(" ", "") in funcdict:
            value = value.replace(";", "")
            value = value.replace(" ", "")
            value = unpack_functions.unpackF(value, funcdict, dict)
    value = stdlibStatements(value, funcdict, dict)
    try:
        eval(value)
    except Exception:
        pass
    finally:
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
    value = "'" + value + "'"
    return str(value)


        
    