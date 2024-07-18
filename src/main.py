# Link all Lascal files
import files
import repl
import sys

print("Lascal v1.1\nq() to exit or .repl to start repl session.")
while True: 
    userinput = input("> ")
    if userinput.startswith(".repl"):
        repl.repl()
    elif userinput.startswith("q()"):
        sys.exit()
    elif len(userinput) < 1:
        pass
    else:
        try:
            files.files(userinput)
        except FileNotFoundError as e:
            print(f"Lascal: {e}")
