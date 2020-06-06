import sys
import os

from VMParser import VMParser
from CodeWriter import CodeWriter

# Challenges:
# - static memory segment (is this done in files?)
# - How to assign *X = *Y (with temp variable?)


def main():
    # Takes as input fileName.vm
    # Outputs fileName.asm
    # Example: python main.py BasicTest/BasicTest.vm
    # Translate BasicTest.vm into BasicTest.asm
    # Check if BasicTest.asm contains nice comments :)
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
        #currentCommand = parser.currentCommand
        commandType = parser.getCommandType()
        if (commandType == parser.C_ARITHMETIC):
            subCommandType = parser.getCommandSubtype()
            if (subCommandType == "add"):
                codeWriter.writeArithmetic(parser.currentCommand)
        print("commandType: " + commandType)


if __name__ == "__main__":
    main()
