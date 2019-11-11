Program TrianguloPascal(output);
 var
 a, b :Integer;
procedure pascal(r, n : Integer);
  var
    i, c, k : Integer;
  begin
        for i := 0 to r-1 do
            begin
            c := n;
            for k := 0 to i do
                begin
                write(c:3);
                write(' ');
                c := ((c * (i-k)) div (k+1));
                end;
            writeln;
            end;
    end;
 
begin
writeln ('Triangulo de Pascal, ingresar el numero de filas y la base del triangulo');
readln( a, b);
if a <> 0 then
    if b <> 0 then
        pascal(a, b)
else
    writeln('Ingresar filas y bases distintas a 0')
    else
    writeln('Ingresar filas y bases distintas a 0')
end.
recetas d eofrtran romeo y julieta
