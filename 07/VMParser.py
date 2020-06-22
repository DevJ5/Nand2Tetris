import os
import re


class VMParser:
    C_ARITHMETIC = "C_ARITHMETIC"
    C_PUSH = "C_PUSH"
    C_POP = "C_POP"
    # TODO:
    C_LABEL = "C_LABEL"
    C_GOTO = "C_GOTO"
    C_IF = "C_IF"  # Is dit if goto?
    C_FUNCTION = "C_FUNCTION"
    C_RETURN = "C_RETURN"
    C_CALL = "C_CALL"

    def __init__(self, file):
        self.file = open(file, "r")
        self.currentCommand = None
        self.commandType = None

    def hasMoreCommands(self):
        cursor = self.file.tell()
        end = os.fstat(self.file.fileno()).st_size
        return cursor != end

    def advance(self):
        while True:
            line = self.file.readline().strip()
            if (not line.startswith("//") and not line == ""):
                break
        self.currentCommand = line
        print("Advance: " + line)

    def getCommandType(self):
        if (self.currentCommand.startswith("push")):
            self.commandType = self.C_PUSH
        elif (self.currentCommand.startswith("pop")):
            self.commandType = self.C_POP
        elif (self.currentCommand.startswith(("add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"))):
            self.commandType = self.C_ARITHMETIC
            # REVIEW: added these new command types
        elif (self.currentCommand.startswith("label")):
            self.commandType = self.C_LABEL
        elif (self.currentCommand.startswith("goto")):
            self.commandType = self.C_GOTO
        elif (self.currentCommand.startswith("if-goto")):
            self.commandType = self.C_IF
        # TODO: rest of the function commands

        return self.commandType or "None"

    def getCommandSubtype(self):
        return self.currentCommand.split(" ")[0]

    def getArg1(self):
        try:
            if (self.commandType == self.C_PUSH or self.commandType == self.C_POP):
                # Return the segment
                return self.currentCommand.split(" ")[1]
            else:
                raise ValueError("CommandType must be push or pop.")
        except ValueError as error:
            print(error)

    def getArg2(self):
        try:
            if (self.commandType == self.C_PUSH or self.commandType == self.C_POP):
                # Return the index
                return self.currentCommand.split(" ")[2]
            else:
                raise ValueError("CommandType must be push or pop.")
        except ValueError as error:
            print(error)

    def closeInputFile(self):
        self.file.close()
