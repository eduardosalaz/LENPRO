! A fortran95 program for G95
! By WQY
program main
implicit none
TYPE jugador
    CHARACTER(50) nombre
    REAL winrate
    INTEGER edad
    LOGICAL campeon
END TYPE jugador

type(jugador) :: Faker
Faker%nombre = "Lee Sang Hyeok"
Faker%winrate = 68.1
Faker%edad = 23
Faker%campeon = .TRUE.

Print*, "Faker: "
Print*, "Nombre: ", Faker%nombre
Print*, "Edad: ", Faker%edad
Print*, "Porcentaje de victorias: ", Faker%winrate
Print*, "Es campeon? ", Faker%campeon
end program main
