// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Pseudo code with GOTO:labels(uppercase) and STORE:variables(lowercase)
// store R0 in n
// store R1 in x
// store 1 in i
// store 0 in sum
// loop from i to n:
    //sum =  sum + x
// check if i == n:
    //jump to STOP label
    //else jump to LOOP
// set R2 to the sum
// END label
// 0 == 0; jump

    @R2
    M = 0 // Set R2 to zero
    @R0
    D = M
    @END // Stop if R0 is zero
    D;JEQ
    @n
    M = D // Set n = R0
    @R1
    D = M
    @END // Stop if R1 is zero
    D;JEQ
    @x
    M = D // Set x = R1
    @i
    M = 0 // i = 0
    //@sum
    //M = 0 // sum = 0
    @n
    D = M
    @POSLOOP // If n is positive jump to positive loop
    D;JGT
    @NEGLOOP // If n is negative jump to negative loop
    D;JLT

(POSLOOP)
    @x
    D = M
    @R2
    M = M + D
    @n
    D = M
    @i
    M = M + 1 // increment i
    D = D - M
    @END
    D;JEQ
    @POSLOOP
    0;JMP
(NEGLOOP)
    @x
    D = M
    @R2
    M = M - D
    @n
    D = M
    @i
    M = M + 1 // increment i
    D = D + M
    @END
    D;JEQ
    @NEGLOOP
    0;JMP

(END)
    @END
    0;JMP



