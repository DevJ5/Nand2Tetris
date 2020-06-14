@256
D = A
@SP
M = D
@Sys.init
0; JMP
// Command: function Sys.init 0
(Sys.init)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_SYS.INIT
D;JEQ
(INIT_LOCALS_SYS.INIT)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_SYS.INIT
D;JNE
(END_INIT_LOCALS_SYS.INIT)
// Command: push constant 4
@4
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: call Main.fibonacci 1   // computes the 4'th fibonacci element
@Sys$ret1
D = A
@SP
AM = M + 1
A = A - 1
M = D
@LCL
D = M
@SP
AM = M + 1
A = A - 1
M = D
@ARG
D = M
@SP
AM = M + 1
A = A - 1
M = D
@THIS
D = M
@SP
AM = M + 1
A = A - 1
M = D
@THAT
D = M
@SP
AM = M + 1
A = A - 1
M = D
@SP
D = M
@5
D = D - A
@1
D = D - A
@ARG
M = D
@SP
D = M
@LCL
M = D
@Main.fibonacci
0; JMP
(Sys$ret1)
// Command: label WHILE
(WHILE)
// Command: goto WHILE              // loops infinitely
@WHILE
0; JMP
