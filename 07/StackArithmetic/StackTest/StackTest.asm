	// eq
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
	// eq
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
	// eq
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
	// lt
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
	// lt
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
	// lt
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
	// gt
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
	// gt
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
	// gt
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
	// add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
	// sub
@SP
AM = M - 1
D = M
A = A - 1
M = M - D
	// neg
@SP
A = M - 1
M = -M
	// and
@SP
AM = M - 1
D = M
A = A - 1
M = M&D
	// or
@SP
AM = M - 1
D = M
A = A - 1
M = M|D
	// not
@SP
A = M - 1
M = !M
