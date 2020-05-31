from hackParser import Parser
from translateCode import TranslateCode
from symbolTable import SymbolTable
import os
import sys
import re

def main():
    # Initialize symbol table with predefined symbols
    symbolTable = SymbolTable()
    initSymbolTable(symbolTable)

    # First pass
    asmFilePath = sys.argv[1]
    firstPass(symbolTable, asmFilePath)
    symbolTable.printSymbolMap()

    # Initialize parser
    parser = Parser(asmFilePath)

    # Open a new file with the same name and a .hack extension
    asmFileName = os.path.basename(asmFilePath)
    hackFileName = f"{asmFileName.split('.')[0]}.hack"
    hackFilePointer = open(f"hackfiles/{hackFileName}", "w")

    # Loop through each instruction and convert it to binary
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
            # If the address is a label or variable
            if address[0].isalpha():
                if not symbolTable.contains(address):
                    symbolTable.addEntry(
                        address, str(symbolTable.ramAddressCounter))
                    symbolTable.incrementRamAddressCounter()
                    symbolTable.printSymbolMap()
                address = symbolTable.getAddress(address)
            print("Address: " + address)
            instruction += '{0:b}'.format(int(address)).zfill(15)
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
        # Skip the L command
        else:
            continue

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


def firstPass(symbolTable, asmFilePath):
    counter = 0
    # Go through line by line
    with open(asmFilePath, "r") as f:
        for line in f:
            line = ''.join(line.split())
            # Ignore empty lines and comments
            if line != '' and not line.startswith('//'):
                # When label is found add label as key, current counter as value
                match = re.search(r'^\((.*)\)$', line)
                print(f"Line: {line}, Counter: {str(counter)}")
                if match:
                    symbolTable.addEntry(match.group(1), str(counter))
                    print(line)
                # Increment counter every line except when label is found
                else:
                    counter += 1


if __name__ == "__main__":
    main()
