import interpret
# Interactive REPL for Lascal

def repl():
    print("REPL for Lascal\nmajor release 1.0\nCtrl-D to exit Lascal or q() to quit REPL.")
    while True:
        userinput = input("> ")
        if userinput.startswith("q()"):
            break
        else:
            interpret.interpret(userinput)
repl()
