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
        # # A counter and reading as long as the line has comments or is an empty line (while loop?)
        while True:
            # Removing all whitespaces in line
            line = ''.join(self.file.readline().split())
            print("line: " + line)
            # Ignore comments and empty lines
            if line != '' and not line.startswith('//'):
                # Take the line up to a potential inline comment
                self.currentCommand = line.split('/')[0]
                print("advance - currentCommand: " + self.currentCommand)
                break

    def getCommandType(self):
        if self.currentCommand.startswith('@'):
            self.commandType = self.commandTypeA
        elif re.search(r'^\(.*\)$', self.currentCommand):
            self.commandType = self.commandTypeL
        else:
            self.commandType = self.commandTypeC
        return self.commandType

    def symbol(self):
        # Return the symbol for A and L commands
        if self.commandType == self.commandTypeA:
            return self.currentCommand[1:]
        if self.commandType == self.commandTypeL:
            return self.currentCommand[1:-1]

    def dest(self):
        print("inside dest" + self.currentCommand)
        if self.commandType == self.commandTypeC:
            match = re.search(r"^([AMD]{1,3})=", self.currentCommand)
            if match:
                return match.group(1)
            else:
                return ''

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
            return ''

    def closeFile(self):
        self.file.close()
