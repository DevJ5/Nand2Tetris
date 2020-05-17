    @i
    M = 0
    @3
    D = A
    @n
    M = D
(LOOP)
    @n
    D = M
    @i
    M = M + 1
    D = D - M // This has to happen, cant do a compare with M underneath the Jump to address.
    @END
    D; JEQ

    @LOOP
    0; JMP

(END)
    @END
    0;JMP
