import sys
import os

from VMParser import VMParser
from CodeWriter import CodeWriter


def main():
    # TODO: file or directory name containing one or more .vm files
    # Outputs fileName/directoryName.asm
    # Example: python main.py FibonacciElement
    # Translate Main.vm and Sys.vm into FibonacciElement.asm

    # Check if program is correctly run
    try:
        # TODO: deze moet directories kunnen ontvangen
        extension = os.path.splitext(sys.argv[1])[1]
        if (extension != ".vm"):
            raise Exception
    except Exception:
        print("Usage: main.py [filename.vm]")
        sys.exit(1)

    # Parse the command line input TODO: check the files in een directory voor .vm files
    vmFilePath = sys.argv[1]
    vmFileName = os.path.basename(vmFilePath)
    vmFileDirectory = os.path.dirname(vmFilePath)

    # TODO: Bootstrap code, SP = 256, Call Sys.init moet als eerste gewrite worden

    # TODO: Hier moet een loop komen die door alle .vm files heenloopt
    # Initialize parser with file to read from
    parser = VMParser(vmFilePath)

    # Initialize codewriter with file to write to
    asmFilePath = os.path.normpath(os.path.join(
        vmFileDirectory, vmFileName.split(".")[0] + ".asm"))
    codeWriter = CodeWriter(asmFilePath)
    # TODO: If er een sys.vm file aanwezig is, doe een init
    # codeWriter.writeInit()

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
            codeWriter.writeLabel(labelName)
        elif (commandType == parser.C_GOTO):
            labelName = parser.getArg1()
            codeWriter.writeGoto(labelName)
        elif (commandType == parser.C_IF):
            labelName = parser.getArg1()
            codeWriter.writeIf(labelName)
        elif (commandType == parser.C_FUNCTION):
            functionName = parser.getArg1()
            numVars = parser.getArg2()
            codeWriter.writeFunction(functionName, numVars)
        elif (commandType == parser.C_RETURN):
            codeWriter.writeReturn()
        else:
            pass

    # Close files after translation has been done
    parser.closeInputFile()
    codeWriter.closeOutputFile()


if __name__ == "__main__":
    main()
