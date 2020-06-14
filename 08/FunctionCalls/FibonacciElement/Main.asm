// Command: function Main.fibonacci 0
(Main.fibonacci)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_MAIN.FIBONACCI
D;JEQ
(INIT_LOCALS_MAIN.FIBONACCI)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_MAIN.FIBONACCI
D;JNE
(END_INIT_LOCALS_MAIN.FIBONACCI)
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
// Command: push constant 2
@2
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: lt                     // checks if n<2
@SP
AM = M - 1
D = M
A = A - 1
D = M - D
M = -1
@LTISTRUE_1
D;JLT
@SP
A = M - 1
M = 0
(LTISTRUE_1)
// Command: if-goto IF_TRUE
@SP
AM = M - 1
D = M
@IF_TRUE
D; JNE
// Command: goto IF_FALSE
@IF_FALSE
0; JMP
// Command: label IF_TRUE          // if n<2, return n
(IF_TRUE)
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
// Command: label IF_FALSE         // if n>=2, returns fib(n-2)+fib(n-1)
(IF_FALSE)
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
// Command: push constant 2
@2
D = A
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
// Command: call Main.fibonacci 1  // computes fib(n-2)
@Main$ret1
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
(Main$ret1)
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
// Command: push constant 1
@1
D = A
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
// Command: call Main.fibonacci 1  // computes fib(n-1)
@Main$ret2
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
(Main$ret2)
// Command: add                    // returns fib(n-1) + fib(n-2)
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
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
