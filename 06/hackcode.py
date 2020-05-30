class TranslateCode:
    _jumpCodes = ['', 'JGT', 'JEQ', 'JGE', 'JLT', 'JNE', 'JLE', 'JMP']

    def __init__(self):
        pass

    def dest(self, mnemonic):
        # needs to be alphabetically sorted
        sortedMnemonic = ''.join(sorted(mnemonic))
        # mnenmonic can be 8 values, None or any combination of AMD
        return {
            'A': '100',
            'D': '010',
            'M': '001',
            'AD': '110',
            'AM': '101',
            'DM': '011',
            'ADM': '111'
        }.get(sortedMnemonic, '000')

    def comp(self, mnemonic):
        print("yo: " + mnemonic)
        return {
            '0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100',
            'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111',
            '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
            'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111',
            'D&A': '0000000', 'D|A': '0010101',
            '': 'xxxxxxx',
            'M': '1110000', '!M': '1110001', '-M': '1110011', 'M+1': '1110111',
            'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
            'D&M': '1000000', 'D|M': '1010101'
        }.get(mnemonic)

    def jump(self, mnemonic):
        idx = self._jumpCodes.index(mnemonic)
        bits = str(bin(idx))[2:].zfill(3)
        return bits
