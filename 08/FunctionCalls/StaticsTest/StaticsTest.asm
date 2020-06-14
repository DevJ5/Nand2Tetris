@256
D = A
@SP
M = D
@Sys.init
0; JMP
// Command: function Class1.set 0
(Class1.set)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_CLASS1.SET
D;JEQ
(INIT_LOCALS_CLASS1.SET)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_CLASS1.SET
D;JNE
(END_INIT_LOCALS_CLASS1.SET)
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
// Command: pop static 0
@SP
AM = M - 1
D = M
@StaticsTest.0
M = D
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
// Command: pop static 1
@SP
AM = M - 1
D = M
@StaticsTest.1
M = D
// Command: push constant 0
@0
D = A
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
// Command: function Class1.get 0
(Class1.get)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_CLASS1.GET
D;JEQ
(INIT_LOCALS_CLASS1.GET)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_CLASS1.GET
D;JNE
(END_INIT_LOCALS_CLASS1.GET)
// Command: push static 0
@StaticsTest.0
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push static 1
@StaticsTest.1
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
// Command: function Class2.set 0
(Class2.set)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_CLASS2.SET
D;JEQ
(INIT_LOCALS_CLASS2.SET)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_CLASS2.SET
D;JNE
(END_INIT_LOCALS_CLASS2.SET)
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
// Command: pop static 0
@SP
AM = M - 1
D = M
@StaticsTest.0
M = D
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
// Command: pop static 1
@SP
AM = M - 1
D = M
@StaticsTest.1
M = D
// Command: push constant 0
@0
D = A
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
// Command: function Class2.get 0
(Class2.get)
@0
D = A
@R13
M = D
@END_INIT_LOCALS_CLASS2.GET
D;JEQ
(INIT_LOCALS_CLASS2.GET)
@SP
AM = M + 1
A = A - 1
M = 0
@R13
M = M - 1
D = M
@INIT_LOCALS_CLASS2.GET
D;JNE
(END_INIT_LOCALS_CLASS2.GET)
// Command: push static 0
@StaticsTest.2
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push static 1
@StaticsTest.3
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
// Command: push constant 6
@6
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: push constant 8
@8
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: call Class1.set 2
@StaticsTest$ret1
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
@2
D = D - A
@ARG
M = D
@SP
D = M
@LCL
M = D
@Class1.set
0; JMP
(StaticsTest$ret1)
// Command: pop temp 0 // Dumps the return value
@SP
AM = M - 1
D = M
@5
M = D
// Command: push constant 23
@23
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: push constant 15
@15
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: call Class2.set 2
@StaticsTest$ret2
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
@2
D = D - A
@ARG
M = D
@SP
D = M
@LCL
M = D
@Class2.set
0; JMP
(StaticsTest$ret2)
// Command: pop temp 0 // Dumps the return value
@SP
AM = M - 1
D = M
@5
M = D
// Command: call Class1.get 0
@StaticsTest$ret3
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
@Class1.get
0; JMP
(StaticsTest$ret3)
// Command: call Class2.get 0
@StaticsTest$ret4
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
@Class2.get
0; JMP
(StaticsTest$ret4)
// Command: label WHILE
(WHILE)
// Command: goto WHILE
@WHILE
0; JMP
