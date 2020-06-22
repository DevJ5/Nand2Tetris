import sys
import os

from VMParser import VMParser
from CodeWriter import CodeWriter


def main():
    # Takes as input fileName.vm or TODO: directory name containing one or more .vm files
    # Outputs fileName.asm
    # Example: python main.py BasicTest/BasicTest.vm
    # Translate BasicTest.vm into BasicTest.asm
    # Check if BasicTest.asm contains nice comments
    # Load BasicTest.asm and BasicTest.tst and check results

    # Check if program is correctly run
    extension = os.path.splitext(sys.argv[1])[1]
    if (extension != ".vm"):
        print("Usage: main.py [filename.vm]")
        sys.exit(1)

    # Parse the command line input
    vmFilePath = sys.argv[1]
    vmFileName = os.path.basename(vmFilePath)
    vmFileDirectory = os.path.dirname(vmFilePath)

    # Initialize parser with file to read from
    parser = VMParser(vmFilePath)

    # Initialize codewriter with file to write to
    asmFilePath = os.path.normpath(os.path.join(
        vmFileDirectory, vmFileName.split(".")[0] + ".asm"))
    codeWriter = CodeWriter(asmFilePath)

    while (parser.hasMoreCommands()):
        parser.advance()
        commandType = parser.getCommandType()
        # Write the command that is being translated as a comment at the start
        codeWriter.writeCommandComment(parser.currentCommand)
        if (commandType == parser.C_ARITHMETIC):
            codeWriter.writeArithmetic(parser.getCommandSubtype())
        elif (commandType == parser.C_PUSH):
            segment = parser.getArg1()
            index = parser.getArg2()
            codeWriter.writePush(parser.getCommandSubtype(), segment, index)
        elif (commandType == parser.C_POP):
            segment = parser.getArg1()
            index = parser.getArg2()
            codeWriter.writePop(parser.getCommandSubtype(), segment, index)
        elif (commandType == parser.C_LABEL):
            labelName = parser.getArg1()
            codeWriter.writeLabel()  # TODO: implement this writeLabel
        elif (commandType == parser.C_GOTO):
            labelName = parser.getArg1()
            codeWriter.writeGoto()  # TODO: implement this writeGoto
        elif (commandType == parser.C_IF):
            labelName = parser.getArg1()
            codeWriter.writeIf()  # TODO: implement this writeIf
        else:
            pass

    # Close files after translation has been done
    parser.closeInputFile()
    codeWriter.closeOutputFile()


if __name__ == "__main__":
    main()
