import textwrap


class CodeWriter:

    def __init__(self, file):
        self.file = open(file, "w")

    def writeArithmetic(self, command):
        if (command == "add"):
            asmCommand = textwrap.dedent("""\
            @SP
            AM = M - 1
            D = M
            A = A - 1
            M = D + M
            """)
        elif (command == "sub"):
            asmCommand = textwrap.dedent("""\
                """)
            # add, sub, neg
            # eq, gt, lt
            # and, or, not

        self.writeCommandComment(command)
        self.file.write(asmCommand)

    def writePushPop(self, command, segment, index):
        # pop segment index
        # push segment index
        return False

    def writeCommandComment(self, command):
        # Write the command that is being translated as a comment at the start
        self.file.write(f"// {command}\n")

    def closeOutputFile(self):
        self.file.close()
