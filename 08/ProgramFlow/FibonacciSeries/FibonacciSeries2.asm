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
// Command: pop pointer 1           // that = argument[1]
@SP
AM = M - 1
D = M
@THAT
M = D
// Command: push constant 0
@0
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop that 0              // first element in the series = 0
@0
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
// Command: push constant 1
@1
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop that 1              // second element in the series = 1
@1
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
// Command: pop argument 0          // num_of_elements -= 2 (first 2 elements are set)
@0
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
// Command: label MAIN_LOOP_START
(MAIN_LOOP_START)
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
// Command: if-goto COMPUTE_ELEMENT // if num_of_elements > 0, goto COMPUTE_ELEMENT
@SP
AM = M - 1
D = M
@COMPUTE_ELEMENT
D; JNE
// Command: goto END_PROGRAM        // otherwise, goto END_PROGRAM
@END_PROGRAM
0; JMP
// Command: label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
// Command: push that 0
@THAT
D = M
@0
A = A + D
D = M
@SP
AM = M + 1
A = A - 1
M = D
// Command: push that 1
@THAT
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
// Command: pop that 2              // that[2] = that[0] + that[1]
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
// Command: push pointer 1
@THAT
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
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
// Command: pop pointer 1           // that += 1
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
// Command: pop argument 0          // num_of_elements--
@0
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
// Command: goto MAIN_LOOP_START
@MAIN_LOOP_START
0; JMP
// Command: label END_PROGRAM
(END_PROGRAM)
