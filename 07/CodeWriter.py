import textwrap


class CodeWriter:

    def __init__(self, file):
        self.file = open(file, "w")
        self.labelCounter = 1

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
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = M - D
                """)
        elif (command == "neg"):
            asmCommand = textwrap.dedent("""\
                @SP
                A = M - 1
                M = -M
                """)
        elif (command == "eq"):
            asmCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                D = M - D
                M = -1
                @EQISTRUE_{self.labelCounter}
                D;JEQ
                @SP
                A = M - 1
                M = 0
                (EQISTRUE_{self.labelCounter})
                """)
            self.labelCounter += 1
        elif (command == "gt"):
            asmCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                D = M - D
                M = -1
                @GTISTRUE_{self.labelCounter}
                D;JGT
                @SP
                A = M - 1
                M = 0
                (GTISTRUE_{self.labelCounter})
                """)
            self.labelCounter += 1
        elif (command == "lt"):
            asmCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                D = M - D
                M = -1
                @LTISTRUE_{self.labelCounter}
                D;JLT
                @SP
                A = M - 1
                M = 0
                (LTISTRUE_{self.labelCounter})
                """)
            self.labelCounter += 1
        elif (command == "and"):
            asmCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = M&D
                """)
        elif (command == "or"):
            asmCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = M|D
                """)
        elif (command == "not"):
            asmCommand = textwrap.dedent(f"""\
                @SP
                A = M - 1
                M = !M
                """)
        else:
            raise ValueError("Arithmetic/logical command not recognized.")

        # Write the command that is being translated as a comment at the start
        self.writeCommandComment(command)
        # Write the assembly command
        self.file.write(asmCommand)

    def writePushPop(self, command, segment, index):
        # pop segment index
        if (command == "pop"):
            if (command == "constant"):
                raise ValueError("Pop can not be used with constant segment.")
            elif (command == "static"):
                pass
            else:
                asmCommand = textwrap.dedent(f"""\
                    @{index}
                    D = A
                    @{segment}
                    D = A + D
                    @R13
                    M = D
                    @SP
                    AM = M - 1
                    D = M
                    @R13
                    A = M
                    M = D
                    """)
        # push segment index
        elif (command == "push"):
            # push constant 7
            if (segment == "constant"):
                asmCommand = textwrap.dedent(f"""\
                @{index}
                D = A
                @SP
                M = D
                """)
            elif (segment == "static"):
                pass
            else:
                asmCommand = textwrap.dedent(f"""\
                @{index}
                D = A
                @{segment}
                A = A + D
                D = M
                @SP
                M = D
                """)
        else:
            raise ValueError("Unrecognized push/pop command.")

        # Write the command that is being translated as a comment at the start
        self.writeCommandComment(command)
        # Write the assembly command
        self.file.write(asmCommand)

    def writeCommandComment(self, command):
        self.file.write(f"\t// {command}\n")

    def closeOutputFile(self):
        self.file.close()
