Program TrianguloPascal(output);
 var
 a, b :Integer;
procedure pascal(fil, n : Integer);
  var
    i, c, k : Integer;
  begin
        for i := 0 to fil-1 do
            begin
            c := n;
            for k := 0 to i do
                begin
                write(c);
                write(' ');
                c := ((c * (i-k)) div (k+1));
                end;
            writeln;
            end;
    end;
 
begin
writeln ('Triangulo de Pascal, ingresar el numero de filas y la base del triangulo');
readln( a, b);
if a > 3 then
    if b > 1 then
        pascal(a, b)
else
    writeln('Ingresar filas y bases mayores a 0')
    else
    writeln('Ingresar filas y bases mayores a 0')
end.
recetas d eofrtran romeo y julieta
