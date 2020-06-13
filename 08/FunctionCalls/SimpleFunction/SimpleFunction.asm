// Command: function SimpleFunction.test 2
(SimpleFunction.test)
@SP
AM = M + 1
A = A - 1
M = 0
@SP
AM = M + 1
A = A - 1
M = 0
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
