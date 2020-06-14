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
// Command: push constant 4000	// test THIS and THAT context save
@4000	//
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
// Command: push constant 5000
@5000
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
// Command: call Sys.main 0
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
@0
D = D - A
@ARG
M = D
@SP
D = M
@LCL
M = D
@Sys.main
0; JMP
(Sys$ret1)
// Command: pop temp 1
@SP
AM = M - 1
D = M
@6
M = D
// Command: label LOOP
(LOOP)
// Command: goto LOOP
@LOOP
0; JMP
// Command: function Sys.main 5
(Sys.main)
@5
D = A
@R13
M = D
@END_INIT_LOCALS_SYS.MAIN
D;JEQ
(INIT_LOCALS_SYS.MAIN)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_SYS.MAIN
D;JNE
(END_INIT_LOCALS_SYS.MAIN)
// Command: push constant 4001
@4001
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
// Command: push constant 5001
@5001
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
// Command: push constant 200
@200
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop local 1
@1
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
// Command: push constant 40
@40
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop local 2
@2
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
// Command: push constant 6
@6
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop local 3
@3
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
// Command: push constant 123
@123
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: call Sys.add12 1
@Sys$ret2
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
@Sys.add12
0; JMP
(Sys$ret2)
// Command: pop temp 0
@SP
AM = M - 1
D = M
@5
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
// Command: push local 2
@LCL
D = M
@2
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push local 3
@LCL
D = M
@3
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push local 4
@LCL
D = M
@4
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
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
// Command: add
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
// Command: function Sys.add12 0
(Sys.add12)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_SYS.ADD12
D;JEQ
(INIT_LOCALS_SYS.ADD12)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_SYS.ADD12
D;JNE
(END_INIT_LOCALS_SYS.ADD12)
// Command: push constant 4002
@4002
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
// Command: push constant 5002
@5002
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
// Command: push constant 12
@12
D = A
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
