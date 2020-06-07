// Command: push constant 10
@10
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop local 0
@0
D = A
@LCL
D = M + D
@R13
M = D
@SP
AM = M - 1
D = M
@R13
A = M
M = D
// Command: push constant 21
@21
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: push constant 22
@22
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop argument 2
@2
D = A
@ARG
D = M + D
@R13
M = D
@SP
AM = M - 1
D = M
@R13
A = M
M = D
// Command: pop argument 1
@1
D = A
@ARG
D = M + D
@R13
M = D
@SP
AM = M - 1
D = M
@R13
A = M
M = D
// Command: push constant 36
@36
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop this 6
@6
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
// Command: push constant 42
@42
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: push constant 45
@45
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop that 5
@5
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
// Command: pop that 2
@2
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
// Command: push constant 510
@510
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop temp 6
@SP
AM = M - 1
D = M
@11
M = D
// Command: push local 0
@LCL
D = M
@0
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push that 5
@THAT
D = M
@5
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
// Command: push argument 1
@ARG
D = M
@1
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
// Command: push this 6
@THIS
D = M
@6
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push this 6
@THIS
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
// Command: sub
@SP
AM = M - 1
D = M
A = A - 1
M = M - D
// Command: push temp 6
@11
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
