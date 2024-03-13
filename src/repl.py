import interpret
# Interactive REPL for Lascal

def repl():
    print("REPL for Lascal\nmajor release 1.0 infoR() for release info\nHELP for help or Ctrl-D to exit Lascal or q() to quit REPL.")
    while True:
        userinput = input("> ")
        if userinput.startswith("q()"):
            break
        elif userinput.startswith("infoR()"):
            print("REPL for Lascal with Lascal version 1.0. REPL version 1.0.0")
        elif userinput.startswith("HELP"):
            print("List of commands:\nANY Lascal Snippet: returns output.\nq(): Exits REPL and returns to interpreter main.\ninfoR(): Release info.\nCtrl-D: Exit Lascal.\nLicense(): Display License.")
        elif userinput.startswith("License()"):
            print("Lascal and Lascal REPL are licensed under the Apache 2.0 license. Read it at: https://www.apache.org/licenses/LICENSE-2.0.html")
        else:
            interpret.interpret(userinput)
repl()
