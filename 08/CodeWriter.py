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
        self.file = open(file, "a")
        self.labelCounter = 1
        self.returnCounter = 1
        self.staticCounter = 0
        self.staticOffset = 0

    def writeInit(self):
        self.file.write(textwrap.dedent(f"""\
            @256
            D = A
            @SP
            M = D
            """))
        self.writeCall("Sys.init", "0")

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
            realIndex = str(int(index) + self.staticOffset)
            asmPushCommand = textwrap.dedent(f"""\
                @{self.fileName}.{realIndex}
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
            realIndex = str(int(index) + self.staticOffset)
            asmPopCommand = textwrap.dedent(f"""\
                @SP
                AM = M - 1
                D = M
                @{self.fileName}.{realIndex}
                M = D
                """)
            self.staticCounter += 1
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
        self.file.write(f"({labelName})\n")

    def writeGoto(self, labelName):
        self.file.write(textwrap.dedent(f"""\
            @{labelName}
            0; JMP
            """))

    def writeIf(self, labelName):
        self.file.write(textwrap.dedent(f"""\
            @SP
            AM = M - 1
            D = M
            @{labelName}
            D; JNE
            """))

    def writeFunction(self, functionName, numVars):
        self.file.write(textwrap.dedent(f"""\
            ({functionName})
            @{numVars}
            D = A
            @R13
            M = D
            @END_INIT_LOCALS_{functionName.upper()}
            D;JEQ
            (INIT_LOCALS_{functionName.upper()})
            @SP
            AM = M + 1
            A = A - 1
            M = 0
            @R13
            M = M - 1
            D = M
            @INIT_LOCALS_{functionName.upper()}
            D;JNE
            (END_INIT_LOCALS_{functionName.upper()})
            """))

    def writeReturn(self):
        self.file.write(textwrap.dedent(f"""\
            @{self.segmentAddresses.get("local")}
            D = M
            @R13
            M = D
            @5
            A = D - A
            D = M
            @R14
            M = D
            @SP
            AM = M - 1
            D = M
            @{self.segmentAddresses.get("argument")}
            A = M
            M = D
            @{self.segmentAddresses.get("argument")}
            D = M + 1
            @SP
            M = D
            @R13
            D = M
            @1
            A = D - A
            D = M
            @{self.segmentAddresses.get("that")}
            M = D
            @R13
            D = M
            @2
            A = D - A
            D = M
            @{self.segmentAddresses.get("this")}
            M = D
            @R13
            D = M
            @3
            A = D - A
            D = M
            @{self.segmentAddresses.get("argument")}
            M = D
            @R13
            D = M
            @4
            A = D - A
            D = M
            @{self.segmentAddresses.get("local")}
            M = D
            @R14
            A = M
            0; JMP
            """))

    def writeCall(self, functionName, numArgs):
        self.file.write(textwrap.dedent(f"""\
            @{self.fileName}$ret{self.returnCounter}
            D = A
            @SP
            AM = M + 1
            A = A - 1
            M = D
            @{self.segmentAddresses.get("local")}
            D = M
            @SP
            AM = M + 1
            A = A - 1
            M = D
            @{self.segmentAddresses.get("argument")}
            D = M
            @SP
            AM = M + 1
            A = A - 1
            M = D
            @{self.segmentAddresses.get("this")}
            D = M
            @SP
            AM = M + 1
            A = A - 1
            M = D
            @{self.segmentAddresses.get("that")}
            D = M
            @SP
            AM = M + 1
            A = A - 1
            M = D
            @SP
            D = M
            @5
            D = D - A
            @{numArgs}
            D = D - A
            @{self.segmentAddresses.get("argument")}
            M = D
            @SP
            D = M
            @{self.segmentAddresses.get("local")}
            M = D
            @{functionName}
            0; JMP
            ({self.fileName}$ret{self.returnCounter})
            """))
        self.returnCounter += 1

    def getTempAddress(self, index):
        baseTempAddress = 5
        return str(baseTempAddress + int(index))

    def writeCommandComment(self, command):
        self.file.write(f"// Command: {command}\n")

    def closeOutputFile(self):
        self.file.close()
