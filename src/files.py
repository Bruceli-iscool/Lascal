import interpret

# File processing
def files(path):
    path = path.rstrip('\n')
    with open(path) as file:
        for line in file:
            line = line.rstrip('\n')
            interpret.interpret(line)
files("/workspaces/Lascal/examples/functions.lasc")