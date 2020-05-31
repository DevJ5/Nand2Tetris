class SymbolTable:
    def __init__(self):
        self.symbolMap = {}
        self.ramAddressCounter = 16

    def addEntry(self, key, value):
        self.symbolMap[key] = value

    def contains(self, key):
        return key in self.symbolMap

    def getAddress(self, key):
        return self.symbolMap.get(key)

    def incrementRamAddressCounter(self):
        self.ramAddressCounter += 1

    def printSymbolMap(self):
        print(self.symbolMap)
