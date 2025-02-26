       IDENTIFICATION DIVISION.
       PROGRAM-ID. MatrixCalculation.

       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.

       01  M-SIZE         PIC 9(4) COMP VALUE 400.

       01  RESULT1        PIC S9(14) COMP VALUE 0.
       01  RESULT2        PIC S9(14) COMP VALUE 0.

       01  TIME1          COMP-2 VALUE 0.
       01  TIME2          COMP-2 VALUE 0.

       01  M1.
           05  M1-ROW OCCURS 400 TIMES.
               10  M1-ELEMENTS OCCURS 400 TIMES PIC S9(10) COMP.
       01  M2.
           05  M2-ROW OCCURS 400 TIMES.
               10  M2-ELEMENTS OCCURS 400 TIMES PIC S9(10) COMP.
       01  M3.
           05  M3-ROW OCCURS 400 TIMES.
               10  M3-ELEMENTS OCCURS 400 TIMES PIC S9(10) COMP.

       01  I              PIC S9(10) COMP.
       01  J              PIC S9(10) COMP.
       01  K              PIC S9(10) COMP.

       01  START-TIME     PIC S9(10) COMP.
       01  END-TIME       PIC S9(10) COMP.

       01  TEMP           PIC S9(10) COMP.

       01  RESULT1_TXT    PIC 9(14).
       01  RESULT2_TXT    PIC 9(14).
       01  TIME1_TXT      PIC 9(3).9(6).
       01  TIME2_TXT      PIC 9(3).9(6).

       PROCEDURE DIVISION.

      * ---------------------------------------------------

           ACCEPT START-TIME FROM TIME.

           MOVE 0 TO RESULT1.

           PERFORM VARYING I FROM 1 BY 1 UNTIL 100 < I
               PERFORM VARYING J FROM 1 BY 1 UNTIL 1000000 < J
                   ADD J TO RESULT1
               END-PERFORM
           END-PERFORM.

           ACCEPT END-TIME FROM TIME.
           COMPUTE TIME1 = (END-TIME - START-TIME) / 100.

      * ---------------------------------------------------

           ACCEPT START-TIME FROM TIME.

           PERFORM VARYING I FROM 1 BY 1 UNTIL M-SIZE < I
               PERFORM VARYING J FROM 1 BY 1 UNTIL M-SIZE < J
                   ADD I TO J GIVING M1-ELEMENTS(I, J)
                   ADD I TO J GIVING M2-ELEMENTS(I, J)
               END-PERFORM
           END-PERFORM.

           PERFORM VARYING I FROM 1 BY 1 UNTIL M-SIZE < I
               PERFORM VARYING J FROM 1 BY 1 UNTIL M-SIZE < J
                   MOVE 0 TO M3-ELEMENTS(I, J)
                   PERFORM VARYING K FROM 1 BY 1 UNTIL M-SIZE < K
                       MULTIPLY M1-ELEMENTS(I, K) BY M2-ELEMENTS(K, J)
                           GIVING TEMP
                       ADD TEMP TO M3-ELEMENTS(I, J)
                   END-PERFORM
               END-PERFORM
           END-PERFORM.

           MOVE 0 TO RESULT2.

           PERFORM VARYING I FROM 1 BY 1 UNTIL M-SIZE < I
               PERFORM VARYING J FROM 1 BY 1 UNTIL M-SIZE < J
                   ADD M3-ELEMENTS(I, J) TO RESULT2
               END-PERFORM
           END-PERFORM.

           ACCEPT END-TIME FROM TIME.
           COMPUTE TIME2 = (END-TIME - START-TIME) / 100.

      * ---------------------------------------------------

           MOVE RESULT1 TO RESULT1_TXT
           MOVE RESULT2 TO RESULT2_TXT
           MOVE TIME1   TO TIME1_TXT
           MOVE TIME2   TO TIME2_TXT
           
           DISPLAY 'COBOL   : Result= ' RESULT1_TXT
                   ', Time= ' TIME1_TXT ' sec'
                   ', Result= ' RESULT2_TXT
                   ', Time= ' TIME2_TXT ' sec'.

       STOP RUN.
