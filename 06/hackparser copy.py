import os
import re


class Parser:
    commandTypeA = "A_COMMAND"
    commandTypeC = "C_COMMAND"
    commandTypeL = "L_COMMAND"

    def __init__(self, file):
        self.file = open(file, "r")
        self.currentCommand = None
        self.commandType = None

    def hasMoreCommands(self):
        cursor = self.file.tell()
        end = os.fstat(self.file.fileno()).st_size
        return cursor != end

    def advance(self):
        # FIXME: comments should be gone as well as empty lines
        # # A counter and reading as long as the line has comments or is an empty line (while loop?)
        self.currentCommand = self.file.readline().rstrip('\r\n')
        print(self.currentCommand)

    def commandType(self):
        print("yes comes here")
        if self.currentCommand.startswith('@'):
            self.commandType = commandTypeA
        elif re.search(r'^\(.*\)$', currentCommand):
            self.commandType = commandTypeL
        else:
            self.commandType = commandTypeC
        return self.commandType

    def symbol(self):
        # Return the symbol for A and L commands
        if self.commandType == commandTypeA:
            return self.currentCommand[1:]
        if self.commandType == commandTypeL:
            return self.currentCommand[1:-1]

    def dest(self):
        if self.currentCommand == commandTypeC:
            match = re.search(r"(^([AMD]{1,3})=", self.currentCommand)
            if match == None:
                return None
            else:
                return match.group(1)
        else:
            return None

    def comp(self):
        # Requires to be a c command
        # Returns the comp mnemonic
        if ";" in self.currentCommand:
            # If it is a jump command
            return self.currentCommand.split(";")[0]
        else:
            # If it is an assign command
            return self.currentCommand.split("=")[1]

    def jump(self):
        # Requires to be a c command
        # Returns the jump mnemonic
        if ";" in self.currentCommand:
            return self.currentCommand.split(";")[1]
        else:
            return None

    def closeFile(self):
        self.file.close()
