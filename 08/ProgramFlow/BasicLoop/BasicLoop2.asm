// Command: push constant 0
@0
D = A
@SP
AM = M + 1
A = A - 1
M = D
// Command: pop local 0         // initializes sum = 0
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
// Command: label LOOP_START
(LOOP_START)
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
// Command: add
@SP
AM = M - 1
D = M
A = A - 1
M = D + M
// Command: pop local 0	        // sum = sum + counter
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
// Command: pop argument 0      // counter--
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
// Command: if-goto LOOP_START  // If counter > 0, goto LOOP_START
@SP
AM = M - 1
D = M
@LOOP_START
D; JNE
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
