import unpack_functions

def if_statement(line, dict, prod, statement):
    if line.startswith("}"):
            if statement:
                unpack_functions.unpack(statement, prod, dict)
                prod[statement] = ""
                type = 0
                return 1
            else:
                return
    elif line == statement:
            pass
    else:
            prod[statement] = prod[statement] + ':' + line