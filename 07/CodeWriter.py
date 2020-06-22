import textwrap
import os


class CodeWriter:
    segmentAddresses = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT"
    }

    def __init__(self, file):
        self.fileName = os.path.basename(file).split(".")[0]
        self.file = open(file, "w")
        self.labelCounter = 1

    def writeArithmetic(self, command):
        if (command == "add"):
            asmArithmeticCommand = textwrap.dedent("""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = D + M
                """)
        elif (command == "sub"):
            asmArithmeticCommand = textwrap.dedent("""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = M - D
                """)
        elif (command == "neg"):
            asmArithmeticCommand = textwrap.dedent("""\
                @SP
                A = M - 1
                M = -M
                """)
        elif (command == "eq"):
            asmArithmeticCommand = textwrap.dedent(f"""\
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
            asmArithmeticCommand = textwrap.dedent(f"""\
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
            asmArithmeticCommand = textwrap.dedent(f"""\
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
            asmArithmeticCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = M&D
                """)
        elif (command == "or"):
            asmArithmeticCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                A = A - 1
                M = M|D
                """)
        elif (command == "not"):
            asmArithmeticCommand = textwrap.dedent(f"""\
                @SP
                A = M - 1
                M = !M
                """)
        else:
            raise ValueError("Arithmetic/logical command not recognized.")

        # Write the assembly command
        self.file.write(asmArithmeticCommand)

    def writePush(self, command, segment, index):
        # Local, argument, this and that
        if (segment in self.segmentAddresses):
            asmPushCommand = textwrap.dedent(f"""\
                @{self.segmentAddresses.get(segment)}
                D = M
                @{index}
                A = A + D
                D = M
                @SP
                AM = M + 1
                A = A - 1
                M = D
                """)
        elif (segment == "constant"):
            asmPushCommand = textwrap.dedent(f"""\
                @{index}
                D = A
                @SP
                AM = M + 1
                A = A - 1
                M = D
                """)
        elif (segment == "static"):
            asmPushCommand = textwrap.dedent(f"""\
                @{self.fileName}.{index}
                D = M
                @SP
                AM = M + 1
                A = A - 1
                M = D
                """)
        elif (segment == "pointer"):
            if (index != "0" and index != "1"):
                raise ValueError("Pointer index can only be 0 or 1.")
            # If index is 0 then it is this, otherwise it is that
            thisOrThat = "this" if index == "0" else "that"
            asmPushCommand = textwrap.dedent(f"""\
                @{self.segmentAddresses.get(thisOrThat)}
                D = M
                @SP
                AM = M + 1
                A = A - 1
                M = D
                """)
        elif (segment == "temp"):
            asmPushCommand = textwrap.dedent(f"""\
                @{self.getTempAddress(index)}
                D = M
                @SP
                AM = M + 1
                A = A - 1
                M = D
                """)
        else:
            raise ValueError("Unrecognized push command.")

        # Write the assembly push command
        self.file.write(asmPushCommand)

    def writePop(self, command, segment, index):
        if (segment in self.segmentAddresses):
            asmPopCommand = textwrap.dedent(f"""\
                @{index}
                D = A
                @{self.segmentAddresses.get(segment)}
                D = M + D
                @R13
                M = D
                @SP
                AM = M - 1
                D = M
                @R13
                A = M
                M = D
                """)
        elif (segment == "constant"):
            raise ValueError("Pop can not be used with constant segment.")
        elif (segment == "static"):
            asmPopCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                @{self.fileName}.{index}
                M = D
                """)
        elif (segment == "pointer"):
            if (index != "0" and index != "1"):
                raise ValueError("Pointer index can only be 0 or 1.")
            # If index is 0 then it is this, otherwise it is that
            thisOrThat = "this" if index == "0" else "that"
            asmPopCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                @{self.segmentAddresses.get(thisOrThat)}
                M = D
                """)
        elif (segment == "temp"):
            asmPopCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                @{self.getTempAddress(index)}
                M = D
                """)
        else:
            raise ValueError("Unrecognized push command.")

        # Write the assembly pop command
        self.file.write(asmPopCommand)

    def writeLabel(self, labelName):
        self.file.write(f"({labelName})")

    def writeGoto(self, labelName):
        self.file.write(f"""\
            @{labelName}
            0; JMP
            """)

    def writeIf(self, labelName):
        self.file.write(f"""\
            @SP
            AM = M - 1
            D = M
            @{labelName}
            D; JNE
            """)

    def getTempAddress(self, index):
        baseTempAddress = 5
        return str(baseTempAddress + int(index))

    def writeCommandComment(self, command):
        self.file.write(f"// Command: {command}\n")

    def closeOutputFile(self):
        self.file.close()
