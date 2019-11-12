print "\n Suma y multiplicacion de Matrices";
print "\Para sumar matrices ingresa 1, Para multiplicar matrices ingresa 2";
$decision = <>;
chomp($decision);
if ($decision == 1) 
{ 
    suma(); 
}
elsif ($decision == 2) 
{ 
    multiplicacion(); 
}

else 
{ 
    print "\n Ingresar una operacion valida"; 
}

sub ingresarMatriz {
  my $xl = $_[0];
  print "\n Ingresar tamaño de columnas y filas " . $xl . ":\n\n";
  print " Numero de filas = ";
  $m = <>;
  chomp($m);
  print " Numero de columnas = ";
  $n = <>;
  chomp($n);
  my @a;
  print "\n Ingresar elementos de la matriz " . $xl . ":\n\n";
  for ($i = 0; $i < $m; $i++) {
    for ($j = 0; $j < $n; $j++) {
      $p = $i+1;
      $q = $j+1;
      print " $xl\[$p,$q\] = ";
      $a[$i][$j] = <>;
      chomp($a[$i][$j]);
    }
  }
  return ($m, $n, @a);
}

sub suma {
  my ($ma1, $na1, @xa) = ingresarMatriz("A");
  my ($ma2, $na2, @ya) = ingresarMatriz("B");
  if (($ma1 == $ma2) && ($na1 == $na2)) {
    for ($i = 0; $i < $ma1; $i++) {
      for ($j = 0; $j <$na1; $j++) {
        $za[$i][$j] = $xa[$i][$j] + $ya[$i][$j];
      }
    }
    system("cls");
    print "\n Suma de Matrices (A+B):\n\n";
    print "\n\tMatriz A:\n\n";
    imprimir(\@xa, $ma1, $na1);
    print "\n\tMatriz B:\n\n";
    imprimir(\@ya, $ma2, $na2);
    print "\n\tMatriz (A+B):\n\n";
    imprimir(\@za, $ma1, $na2);
  } else {
    print "\n La suma no es posible";
    print "\n El numero de filas y columnas no es adecuado.\n";
  }
}
sub multiplicacion {
  my ($mm1, $nm1, @xm) = ingresarMatriz("A");
  my ($mm2, $nm2, @ym) = ingresarMatriz("B");
  if ($nm1 == $mm2) {
    for ($i = 0; $i < $mm1; $i++) {
      for ($j = 0; $j < $nm2; $j++) {
        $zm[$i][$j] = 0;
        for ($k = 0; $k < $nm1; $k++) {
          $zm[$i][$j] += ($xm[$i][$k] * $ym[$k][$j]);
        }
      }
    }
    system("cls");
    print "\n Multiplicacion de Matrices (AxB):\n\n";
    print "\n\tMatriz A:\n\n";
    imprimir(\@xm, $mm1, $nm1);
    print "\n\tMatriz B:\n\n";
    imprimir(\@ym, $mm2, $nm2);
    print "\n\tMatriz (AxB):\n\n";
    imprimir(\@zm, $mm1, $nm2);
  } else {
    print "\n La multiplicacion no es posible.";
    print "\n El numero de filas y columnas no es adecuado.\n";
  }
}
sub imprimir {
  my @x = @{$_[0]};
  my $m = $_[1];
  my $n = $_[2];
  print "\t\t";
  for ($i = 0; $i < $m; $i++) {
    for ($j = 0; $j < $n; $j++) {
      printf("%8s", $x[$i][$j]);
    }
    print "\n\n\n\t\t";
  }
}

<>;
