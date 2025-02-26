program MatrixMultiplication;

uses
    SysUtils, Time;

const
    M_SIZE = 400;

var
    i, j, k              : LongInt;
    start_time, end_time : TDateTime;
    time                 : Double;
    m1, m2, m3           : array[1..M_SIZE, 1..M_SIZE] of LongInt;
    result               : QWord;

begin

    start_time := Now;

    for i := 1 to M_SIZE do
        for j := 1 to M_SIZE do
            begin
                m1[i, j] := i + j;
                m2[i, j] := i + j
            end;

    for i := 1 to M_SIZE do
        for j := 1 to M_SIZE do
            begin
                m3[i, j] := 0;
                for k := 1 to M_SIZE do
                    m3[i, j] := m3[i, j] + m1[i, k] * m2[k, j]
            end;

    result := 0;
    for i := 1 to M_SIZE do
        for j := 1 to M_SIZE do
            result := result + m3[i, j];

    end_time := Now;
    time := (end_time - start_time) * 24 * 60 * 60;

    (* --------------------------------------------------------------------------- *)
  
    WriteLn(Format('Result= %d, Time= %10.6f sec', [result1, time1, result, time2]))

end.
