from hackParser import Parser
from translateCode import TranslateCode
from symbolTable import SymbolTable
import os
import sys

#  TODO: When done remove all print statements


def main():
    # Initialize symbol table with predefined symbols
    symbolTable = SymbolTable()
    initSymbolTable(symbolTable)
    symbolTable.printSymbolMap()
    sys.exit()

    # Initialize parser
    asmFilePath = sys.argv[1]
    parser = Parser(asmFilePath)

    # First pass
    parser.setLabelsInSymbolTable(symbolTable)

    asmFileName = os.path.basename(asmFilePath)
    # Open a new file with the same name and a .hack extension
    hackFileName = f"{asmFileName.split('.')[0]}.hack"
    hackFilePointer = open(f"hackfiles/{hackFileName}", "w")

    while parser.hasMoreCommands():
        instruction = ""
        parser.advance()
        commandType = parser.getCommandType()
        print("commandType: " + commandType)
        if commandType == parser.commandTypeA:
            # Opcode
            instruction += '0'
            # Address
            address = parser.symbol()
            print("Address: " + str(address))
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
            # for the L command (LOOP)
            else:
                pass

        # Write the instruction line to the hack file
        hackFilePointer.write(instruction + "\n")

    # Clean up
    parser.closeFile()
    hackFilePointer.close()


def initSymbolTable(symbolTable):
    symbolTable.addEntry('SP', '0')
    symbolTable.addEntry('LCL', '1')
    symbolTable.addEntry('ARG', '2')
    symbolTable.addEntry('THIS', '3')
    symbolTable.addEntry('THAT', '4')
    for i in range(0, 16):
        symbolTable.addEntry(f'R{i}', f'{i}')
    symbolTable.addEntry('SCREEN', '16384')
    symbolTable.addEntry('KBD', '24576')


def firstPass(symbolTable):
    pass


if __name__ == "__main__":
    main()
