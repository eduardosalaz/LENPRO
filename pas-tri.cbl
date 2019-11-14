            IDENTIFICATION DIVISION.
            PROGRAM-ID. triangulo_pas.

            DATA DIVISION.
              WORKING-STORAGE SECTION.
              01 CONTADOR PIC 999 VALUE 1.
              01 POTENCIA PIC 999 VALUE 1.
              01 TERMINO PIC 999 VALUE 1.
              01 OP PIC 9999999 VALUE 1.
              01 N PIC S9(11)9999999.
              01 DOP PIC 999 VALUE 1.
              01 DIF PIC 999 VALUE 1.
              01 DEN1 PIC 9999999 VALUE 1.
              01 DEN2 PIC 9999999 VALUE 1.
              01 FACT PIC 9999999 VALUE 1.
            PROCEDURE DIVISION.
            
              DISPLAY "                         " WITH NO ADVANCING.
              DISPLAY "TRIANGULO DE PASCAL".
              Accept N.
              IF N > 0 THEN
                PERFORM Ciclo WITH TEST AFTER
                VARYING POTENCIA FROM 1 BY 1
                UNTIL POTENCIA = 10
                DISPLAY "                        " WITH NO ADVANCING
              ELSE
                DISPLAY "INGRESAR NUMERO VALIDO"
              END-IF.
              STOP RUN.
              
              Ciclo.
                COMPUTE FACT = 14 - POTENCIA.
                PERFORM CicloTabs WITH TEST AFTER
                    VARYING CONTADOR FROM 1 BY 1
                    UNTIL CONTADOR = FACT.
                PERFORM CICLO2 WITH TEST AFTER
                    VARYING TERMINO FROM 0 BY 1
                    UNTIL TERMINO = POTENCIA.
                DISPLAY "  ".
              Ciclo2.
                MOVE N TO OP.
                MOVE 1 TO DEN1.
                MOVE 1 TO DEN2.
                COMPUTE DIF = POTENCIA - TERMINO.
                PERFORM CicloFac WITH TEST AFTER
                    VARYING CONTADOR FROM 1 BY 1
                    UNTIL CONTADOR = POTENCIA.
                PERFORM CicloIndent WITH TEST AFTER
                    VARYING CONTADOR FROM 1 BY 1
                    UNTIL CONTADOR = TERMINO.
                PERFORM CicloIndent2 WITH TEST AFTER
                    VARYING CONTADOR FROM 1 BY 1
                    UNTIL CONTADOR = DIF.
                COMPUTE OP = OP / DEN1.
                COMPUTE OP = OP / DEN2.
                MOVE OP TO DOP.
                DISPLAY DOP WITH NO ADVANCING.
                DISPLAY "   " WITH NO ADVANCING.
              CicloFac.
                COMPUTE OP = OP * CONTADOR.
              CicloIndent.
                COMPUTE DEN1 = DEN1 * CONTADOR.
              CicloIndent2.
                COMPUTE DEN2 = DEN2 * CONTADOR.
              CicloTabs.
                Display "  " WITH NO ADVANCING.
