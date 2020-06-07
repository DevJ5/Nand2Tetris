// Command: push constant 3030
@3030
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop pointer 0
@SP
AM = M - 1
D = M
@THIS
M = D
// Command: push constant 3040
@3040
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop pointer 1
@SP
AM = M - 1
D = M
@THAT
M = D
// Command: push constant 32
@32
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop this 2
@2
D = A
@THIS
D = M + D
@R13
M = D
@SP
AM = M - 1
D = M
@R13
A = M
M = D
// Command: push constant 46
@46
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop that 6
@6
D = A
@THAT
D = M + D
@R13
M = D
@SP
AM = M - 1
D = M
@R13
A = M
M = D
// Command: push pointer 0
@THIS
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push pointer 1
@THAT
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
// Command: push this 2
@THIS
D = M
@2
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: sub
@SP
AM = M - 1
D = M
A = A - 1
M = M - D
// Command: push that 6
@THAT
D = M
@6
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
