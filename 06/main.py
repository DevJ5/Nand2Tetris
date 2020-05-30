from hackparser import Parser
from hackcode import MachineCode

import sys


def main():
    asmFileName = sys.argv[1]
    parser = Parser(asmFileName)
    # Open a new file with the same name and a .hack extension
    hackFileName = f"{asmFileName.split(".")[0]}.hack"
    hackFilePointer = open(hackFileName, "w")

    while parser.hasMoreCommands():
        instruction = ""
        parser.advance()
        commandType = parser.commandType()
        if commandType == parser.commandTypeA:
            # Opcode
            instruction += '0'
            # Address
            address = parser.symbol()
            instruction += '{0:b}'.format(address).zfill(15)
        elif commandType == parser.commandTypeC:
            # Opcode
            instruction += '1'
            # Nop
            instruction += '11'
            # Comp (6 bits)
            compMnemonic = parser.comp()
            translateCode = TranslateCode()
            compBits = translateCode.comp(compMnemonic)
            instruction += compBits
            # Destination (3 bits)
            destinationMnemonic = parser.dest()
            destinationBits = translateCode.dest(destinationMnemonic)
            instruction += destinationBits
            # Jump (3 bits)
            jumpMnemonic = parser.jump()
            jumpBits = translateCode.jump(jumpMnemonic)
            instruction += jumpBits

        # TODO:
        # else: for the L command (LOOP)

        # Write the instruction line to the hack file
        hackFilePointer.write(instruction)

    # Clean up
    parser.closeFile()
    hackFilePointer.close()


if __name__ == "__main__":
    main()
