use warnings;
my $celsius = "Celsius";
my $fahrenheit = "Fahrenheit";
my $kelvin = "Kelvin";
my $rankine = "Rankine";
print "Programa para convertir temperaturas en Celsius, Fahrenheit, Kelvin y Rankine\n";
print "Ingresar la escala inicial de temperatura empezando con mayúscula";
$escala_inicial=<STDIN>;
chomp ($escala_inicial);
if ($escala_inicial eq $celsius)
    {
        print "Ingresar la temperatura inicial en grados";
        $temp_inicial=<STDIN>;
        chomp ($temp_inicial);
        if ($temp_inicial > -274)
            {
                print "Ingresar el nombre completo de la escala a convertir empezando con mayúscula";
                $escala_final=<STDIN>;
                chomp ($escala_final);
                if($escala_final eq $fahrenheit)
                    {
                       $temp_final = ($temp_inicial *1.8) +32;
                       print "La temperatura en " . $escala_final . " es " . $temp_final;
                    }
                elsif($escala_final eq $kelvin)
                    {
                        $temp_final=($temp_inicial + 273.15);
                        print "La temperatura en " . $escala_final . " es " . $temp_final;
                    }
                elsif($escala_final eq $rankine)
                    {
                        $temp_final= ($temp_inicial + 273.15) *1.8;
                        print "La temperatura en " . $escala_final . " es " . $temp_final;
                    }
                else
                {
                    print "Ingresar una escala valida";
                }            
            }
        else
            {
                print "Ingresar una temperatura valida";
            }    
    }
elsif ($escala_inicial eq $fahrenheit)
    {
        print "Ingresar la temperatura inicial en grados";
        $temp_inicial=<STDIN>;
        chomp ($temp_inicial);
        if($temp_inicial > -459.67)
        {
            print "Ingresar el nombre completo de la escala a convertir empezando con mayúscula";
            $escala_final=<STDIN>;
            chomp($escala_final);
            if ($escala_final eq $celsius)
                {
                    $temp_final = ($temp_inicial -32) *0.555;
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            elsif($escala_final eq $kelvin)
                {
                    $temp_final = ($temp_inicial +459.67) *0.555;
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            elsif ($escala_final eq $rankine)
                {
                    $temp_final = ($temp_inicial +459.67);
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            else 
                {
                    print "Ingresar una escala valida";
                }
        }
        else 
        {
            print "Ingresar una temperatura valida";
        }
    }
elsif ($escala_inicial eq "Kelvin")
    {
        print "Ingresar la temperatura inicial en grados";
        $temp_inicial=<STDIN>;
        chomp ($temp_inicial);
        if($temp_inicial > -1)
        {
            print "Ingresar el nombre completo de la escala a convertir empezando con mayúscula";
            $escala_final=<STDIN>;
            chomp ($escala_final);
            if ($escala_final eq $celsius)
                {
                    $temp_final = ($temp_inicial -273.15);
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            elsif ($escala_inicial eq $fahrenheit)
                {
                    $temp_final = ($temp_inicial * 1.8) -459.67;
                    print "La temperatura en " . $escala_final . "es " . $temp_final;

                }
            elsif ($escala_final eq $rankine)
                {
                    $temp_final = ($temp_inicial *1.8);
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            else
                {
                    print "Ingresar una escala valida";
                }
        }
        else
            {
                print "Ingresar una temperatura valida"
            }
    }
elsif ($escala_inicial eq "Rankine")
    {
        print "Ingresar la temperatura inicial en grados";
        $temp_inicial=<STDIN>;
        chomp ($temp_inicial);
        if($temp_inicial > -1)
        {
            print "Ingresar el nombre completo de la escala a convertir empezando con mayúscula";
            $escala_final=<STDIN>;
            chomp ($escala_final);
            if ($escala_final eq $celsius)
                {
                    $temp_final = ($temp_inicial -491.67) /1.8;
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            elsif ($escala_inicial eq $fahrenheit)
                {
                    $temp_final = ($temp_inicial - 459.67);
                    print "La temperatura en " . $escala_final . "es " . $temp_final;

                }
            elsif ($escala_final eq $kelvin)
                {
                    $temp_final = ($temp_inicial /1.8);
                    print "La temperatura en " . $escala_final . "es " . $temp_final;
                }
            else
                {
                    print "Ingresar una escala valida";
                }
        }
        else
            {
                print "Ingresar una temperatura valida"
            }
    }
else 
    {
        print "Ingresar una escala valida"
    }
