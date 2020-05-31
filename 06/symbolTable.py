class SymbolTable:
    def __init__(self):
        self.symbolMap = {}

    def addEntry(self, key, value):
        self.symbolMap[key] = value

    def contains(self, key):
        return key in self.symbolMap

    def getAddress(self, key):
        return self.symbolMap.get(key)

    def printSymbolMap(self):
        print(self.symbolMap)
