      PROGRAM FACTORIAL                                                 0000010
C     THIS PROGRAM COMPUTES THE FACTORIAL OF A GIVEN NUMBER             0000020
      INTEGER N, FACT, I                                                0000030
      PRINT *, 'ENTER A POSITIVE INTEGER:'                              0000040
      READ *, N                                                         0000050
      IF (N .LT. 0) THEN                                                0000060
          PRINT *, 'INVALID INPUT! MUST BE POSITIVE.'                   0000070
          STOP                                                          0000080
      ENDIF                                                             0000090
      FACT = 1                                                          0000100
      I = 1                                                             0000110
  100 IF (I .GT. N) GOTO 200                                            0000120
      FACT = FACT * I                                                   0000130
      I = I + 1                                                         0000140
      GOTO 100                                                          0000150
  200 PRINT 300, N, FACT                                                0000160
C     OUTPUT THE RESULT                                                 0000170
  300 FORMAT(' FACTORIAL OF ',                                          0000180
     &       I4,                                                        0000181
     &       ' IS ',                                                    0000182
     &       I10)                                                       0000183
C     END OF PROGRAM                                                    0000190
      END                                                               0000200
