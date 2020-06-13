// Command: function SimpleFunction.test 2
(SimpleFunction.test)
@2
D = A
@R13
M = D
@END_INIT_LOCALS
D;JEQ
(INIT_LOCALS)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS
D;JNE
(END_INIT_LOCALS)
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
// Command: push local 1
@LCL
D = M
@1
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
// Command: not
@SP
A = M - 1
M = !M
// Command: push argument 0
@ARG
D = M
@0
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
// Command: return
@LCL
D = M
@R13
M = D
@5
A = D - A
D = M
@R14
M = D
@SP
AM = M - 1
D = M
@ARG
A = M
M = D
@ARG
D = M + 1
@SP
M = D
@R13
D = M
@1
A = D - A
D = M
@THAT
M = D
@R13
D = M
@2
A = D - A
D = M
@THIS
M = D
@R13
D = M
@3
A = D - A
D = M
@ARG
M = D
@R13
D = M
@4
A = D - A
D = M
@LCL
M = D
@R14
A = M
0; JMP
