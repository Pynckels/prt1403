      PROGRAM TEST

        REAL*16, PARAMETER :: PI = 4 * ATAN(1.0_16)

        INTEGER :: i = PI
        REAL    :: r = PI
        REAL*8  :: s = PI
        REAL*16 :: t = PI

        PRINT "(i4)", i
        PRINT *, r
        PRINT *, s
        PRINT *, t

      END PROGRAM TEST
