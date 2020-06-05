// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(RESTART)
    @SCREEN // Address 16384
    D = A
    @startaddr // Set the start address (address of screen)
    M = D
    @KBD // Address 24576
    D = A
    @endaddr // Set the end address (address of keyboard)
    M = D

    @KBD
    D = M
    @DRAWBLACKLOOP // If keyboard is pressed jump to drawloop
    D; JGT
    @DRAWWHITELOOP // If keyboard is pressed jump to drawloop
    D; JEQ

(DRAWBLACKLOOP)
    @KBD
    D = M
    @RESTART // If keyboard is not pressed jump back to restart
    D; JEQ
    @startaddr
    A = M
    M = -1 // Set register to black
    @startaddr
    M = M + 1 // increment startaddr
    @endaddr
    D = M
    @startaddr
    D = D - M
    @RESTART // End the loop if start address has reached end address
    D;JEQ
    @DRAWBLACKLOOP
    0; JMP // Go the beggining of drawloop
    
(DRAWWHITELOOP)
    @KBD
    D = M
    @RESTART // If keyboard is pressed jump back to restart
    D; JGT


    @startaddr
    A = M
    M = 0 // Set register to white

    @startaddr
    M = M + 1 // increment startaddr

    @endaddr
    D = M
    @startaddr
    D = D - M
    @RESTART // End the loop if start address has reached end address
    D;JEQ
    @DRAWWHITELOOP
    0; JMP // Go the beggining of drawloop