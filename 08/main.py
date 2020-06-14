import sys
import os
import glob
import traceback

from VMParser import VMParser
from CodeWriter import CodeWriter


def main():
    # File or directory name containing one or more .vm files
    # Outputs fileName/directoryName.asm
    # Example: python main.py FibonacciElement
    # Translate Main.vm and Sys.vm into FibonacciElement.asm

    absPath = os.path.abspath(sys.argv[1])
    isDirectory = os.path.isdir(absPath)
    asmFileName = ""
    try:
        if (isDirectory):
            os.chdir(absPath)
            listOfVmFiles = [file for file in glob.glob("*.vm")]
            asmFileName = os.path.basename(absPath)
        else:
            # Check if it is a .vm file
            os.chdir(os.path.dirname(absPath))
            fileName = os.path.basename(absPath)
            if (not fileName.endswith(".vm")):
                raise ValueError("Usage: main.py[filename.vm]")
            listOfVmFiles = [fileName]
            asmFileName = fileName.split(".")[0]
    except ValueError as e:
        print(e.message)
        sys.exit(1)
    except:
        traceback.print_exc()
        sys.exit(1)

    # Initialize codewriter with file to write to
    asmFilePath = os.path.normpath(os.path.join(asmFileName + ".asm"))
    codeWriter = CodeWriter(asmFilePath)

    # If there is a Sys.vm file write the init code
    if "Sys.vm" in listOfVmFiles:
        codeWriter.writeInit()

    # Initialize parser with file to read from
    print(listOfVmFiles)

    for file in listOfVmFiles:
        parser = VMParser(file)

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
                codeWriter.writePush(
                    parser.getCommandSubtype(), segment, index)
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
            elif (commandType == parser.C_CALL):
                functionName = parser.getArg1()
                numArgs = parser.getArg2()
                codeWriter.writeCall(functionName, numArgs)
            else:
                pass

        # Close input file after translation has been done
        parser.closeInputFile()
        # Increment static offset for the next file
        codeWriter.staticOffset += codeWriter.staticCounter
        codeWriter.staticCounter = 0

    # Close output file after all files are translated
    codeWriter.closeOutputFile()


if __name__ == "__main__":
    main()
