// Command: push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: eq
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@EQISTRUE_1
D;JEQ
@SP
A = M - 1
M = 0
(EQISTRUE_1)
// Command: push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 16
@16
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: eq
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@EQISTRUE_2
D;JEQ
@SP
A = M - 1
M = 0
(EQISTRUE_2)
// Command: push constant 16
@16
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 17
@17
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: eq
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@EQISTRUE_3
D;JEQ
@SP
A = M - 1
M = 0
(EQISTRUE_3)
// Command: push constant 892
@892
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 891
@891
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: lt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@LTISTRUE_4
D;JLT
@SP
A = M - 1
M = 0
(LTISTRUE_4)
// Command: push constant 891
@891
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 892
@892
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: lt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@LTISTRUE_5
D;JLT
@SP
A = M - 1
M = 0
(LTISTRUE_5)
// Command: push constant 891
@891
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 891
@891
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: lt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@LTISTRUE_6
D;JLT
@SP
A = M - 1
M = 0
(LTISTRUE_6)
// Command: push constant 32767
@32767
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: gt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@GTISTRUE_7
D;JGT
@SP
A = M - 1
M = 0
(GTISTRUE_7)
// Command: push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 32767
@32767
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: gt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@GTISTRUE_8
D;JGT
@SP
A = M - 1
M = 0
(GTISTRUE_8)
// Command: push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 32766
@32766
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: gt
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@GTISTRUE_9
D;JGT
@SP
A = M - 1
M = 0
(GTISTRUE_9)
// Command: push constant 57
@57
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 31
@31
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: push constant 53
@53
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
// Command: push constant 112
@112
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: sub
@SP
AM = M - 1
D = M
A = A - 1
M = M - D
// Command: neg
@SP
A = M - 1
M = -M
// Command: and
@SP
AM = M - 1
D = M
A = A - 1
M = M&D
// Command: push constant 82
@82
D = A
@SP
M = M + 1
A = M - 1
M = D
// Command: or
@SP
AM = M - 1
D = M
A = A - 1
M = M|D
// Command: not
@SP
A = M - 1
M = !M
