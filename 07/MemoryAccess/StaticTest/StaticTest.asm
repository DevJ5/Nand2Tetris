// Command: push constant 111
@111
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: push constant 333
@333
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: push constant 888
@888
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop static 8
@SP
AM = M - 1
D = M
@StaticTest.8
M = D
// Command: pop static 3
@SP
AM = M - 1
D = M
@StaticTest.3
M = D
// Command: pop static 1
@SP
AM = M - 1
D = M
@StaticTest.1
M = D
// Command: push static 3
@StaticTest.3
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push static 1
@StaticTest.1
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
// Command: push static 8
@StaticTest.8
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
