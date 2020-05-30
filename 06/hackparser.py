import os
import re


class Parser:
	commandTypeA = "A_COMMAND"
	commandTypeC = "C_COMMAND"
	commandType: = "L_COMMAND"

    def __init__(self, file):
        self.file = open(file, "r")
        self.currentCommand = None
        self.commandType = None

    def hasMoreCommands(self):
        cursor = self.file.tell()
        end = os.fstat(self.file.fileno()).st_size
        return cursor != end

    def advance(self):
		# FIXME: comments should be gone 
        self.currentCommand = self.file.readline().rstrip('\r\n')
        print(self.currentCommand)

    def commandType():
        if currentCommand.startswith('@'):
            self.commandType = commandTypeA
        elif re.search(r'^\(.*\)$', currentCommand):
            self.commandType = commandTypeL
		else:
			self.commandType = commandTypeC
	
	def symbol():
		if self.commandType = commandTypeA
			return self.currentCommand[1:]
		if self.commandType = commandTypeL:
			return self.currentCommand[1:-1]
	
	def dest():
		if self.currentCommand = commandTypeC:
			match = re.search(r"(^([AMD]{1,3})=", self.currentCommand)
			if match == None:
				return None
			else:
				return match.group(1)
		else:
			return None
	
	def comp():
		

    def closeFile(self):
        self.file.close()
