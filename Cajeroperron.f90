Program Cajero
implicit NONE


type dinero
integer,dimension(3)::bdt
integer, dimension(4)::mxn
end type dinero
type (dinero):: c
integer,dimension(4)::mxnsale
integer,dimension(3)::bdtsale
real :: pesosres = 50
real:: takares = 100
integer :: takaresint =100
integer :: pesosresint = 50
integer :: n,ierror,jerror,redondea,sale,i, entraint
real :: residuo,entra
do i=1,4
c%mxn(i)=125
mxnsale(i)=0
end do

do i=1,3
c%bdt(i)=166
bdtsale(i)=0
end do

open(2,file="dinero.txt")
   write(2,*)'Billetes MXN       $500        $200       $100        $50'
    write(2,*)'          ', c%mxn
   write(2,*)'Billetes        $1000       $500        $100       '
    write(2,*)'          ', c%bdt

do
  print *,' Cajero ATM'
  print *,'Escoga una opcion'
  print *,' '
  print *,'1) Retirar Pesos Mexicanos (MXN)'
  print *,'2) Retirar Taka Banglades (BDT)'
  print *,'3) Conertir de Pesos Mexicanos (MXN) a Taka Banglades (BDT) y retirar Taka Banglades (BDT)'
  print *,'4) Convertir de Taka Banglades (BDT) a Pesos Mexicanos (MXN) y retirar Pesos Mexicanos (MXN)'
  read(*,'(i10)',iostat=ierror) n

    if ( ierror == 0 .and. n <5 .and. n>0 ) then
      exit
    endif
    write(*,*) 'Introducir solo numeros entre 1 y 4 (Enteros)'

end do

select case (n)
case(1)
do
  print*, ' Cuanto dinero desea retirar (Solo multiplos de 50)(digitos enteros)'
    print*, ' Maximo $6,000.00 MXN'
    print*,''
  read(*,'(i10)',iostat=ierror) entra
    if ( ierror == 0 .and. entra <=6000 .and. entra>0 ) then
     residuo=mod(entra,pesosres)
     if(residuo==0)then
      exit
      end if
    endif
    write(*,*) 'Introducir una cantidad valida'
end do
sale=entra
    do
        if(sale==0)THEN
        exit
        end if
        sale=sale-500
        if(sale>0)THEN
            mxnsale(1)=mxnsale(1)+1
        ELSE
        sale=sale+500
        end if
        sale=sale-200
        if(sale>0)THEN
            mxnsale(2)=mxnsale(2)+1
        ELSE
            sale=sale+200
        end if
        sale=sale-100
        if(sale>0)THEN
            mxnsale(3)=mxnsale(3)+1
        ELSE
            sale=sale+100
        end if
        sale=sale-50
        if(sale>=0)THEN
            mxnsale(4)=mxnsale(4)+1
        ELSE
            sale=sale+50
        end if
    end do
    
    do i=1,4
    c%mxn(i)=c%mxn(i)-mxnsale(i)
    end do
    write(2,*)'Billetes MXN       $500        $200       $100        $50'
    write(2,*)'          ', c%mxn
    print*, '        $500        $200        $100         $50'
    print*,mxnsale
case(2)
do
  print*, ' Cuanto dinero desea retirar (Solo multiplos de 100)(digitos enteros)'
    print*, ' Maximo $100,000.00 BDT'
    print*,''
  read(*,'(i10)',iostat=ierror) entra
    if ( ierror == 0 .and. entra <=100000 .and. entra>0 ) then
     residuo=mod(entra,takares)
     if(residuo==0)then
      exit
      end if
    endif
    write(*,*) 'Introducir una cantidad valida'
end do
sale=entra
    do
        if(sale==0)THEN
        exit
        end if
        sale=sale-1000
        if(sale>0)THEN
            bdtsale(1)=bdtsale(1)+1
        ELSE
        sale=sale+1000
        end if
        sale=sale-500
        if(sale>0)THEN
            bdtsale(2)=bdtsale(2)+1
        ELSE
            sale=sale+500
        end if
        sale=sale-100
        if(sale>=0)THEN
            bdtsale(3)=bdtsale(3)+1
        ELSE
            sale=sale+100
        end if

    end do
    
    do i=1,4
    c%bdt(i)=c%bdt(i)-bdtsale(i)
    end do
   write(2,*)'Billetes        $1000       $500        $100       '
    write(2,*)'          ', c%bdt
    print*,'Billetes        $1000       $500        $100       '
    print*,bdtsale
case(3)
do
 print*, ' Cuanto dinero desea convertir de MXN a BDT (Se redondeara para poder retirar la cantidad deseada)'
    print*, ' Maximo $6,000.00 MXN'
    print*,''
  read(*,'(i10)',iostat=ierror) entra
  if(entra<=6000 .and. entra>0)THEN
    entra=entra*4.33992323
    entraint=entra
     residuo=mod(entraint,takaresint)
    do while(residuo .ne. 0)
        entraint=entraint-1
        residuo=mod(entraint,takaresint)
    end do
    sale=entra
    do
        if(sale==0)THEN
        exit
        end if
        sale=sale-1000
        if(sale>0)THEN
            bdtsale(1)=bdtsale(1)+1
        ELSE
        sale=sale+1000
        end if
        sale=sale-500
        if(sale>0)THEN
            bdtsale(2)=bdtsale(2)+1
        ELSE
            sale=sale+500
        end if
        sale=sale-100
        if(sale>=0)THEN
            bdtsale(3)=bdtsale(3)+1
        ELSE
            sale=sale+100
        end if

    end do
  end if

end do
  do i=1,4
    c%bdt(i)=c%bdt(i)-bdtsale(i)
    end do
   write(2,*)'Billetes        $1000       $500        $100       '
    write(2,*)'          ', c%bdt
    print*,'Billetes        $1000       $500        $100       '
    print*,bdtsale
case(4)
do 
print*, ' Cuanto dinero desea convertir de BDT a MXN (Se redondeara para poder retirar la cantidad deseada)'
    print*, ' Maximo $100,000.00 BDT'
    print*,''
     read(*,'(i10)',iostat=ierror) entra
      if(entra<=100000 .and. entra>0)THEN
      entra=entra*0.230418822
       entraint=entra
         residuo=mod(entraint,pesosresint)
          do while(residuo .ne. 0)
            entraint=entraint-1
            residuo=mod(entraint,pesosresint)
          end do
          sale=entra
    do
        if(sale==0)THEN
        exit
        end if
        sale=sale-500
        if(sale>0)THEN
            mxnsale(1)=mxnsale(1)+1
        ELSE
        sale=sale+500
        end if
        sale=sale-200
        if(sale>0)THEN
            mxnsale(2)=mxnsale(2)+1
        ELSE
            sale=sale+200
        end if
        sale=sale-100
        if(sale>0)THEN
            mxnsale(3)=mxnsale(3)+1
        ELSE
            sale=sale+100
        end if
        sale=sale-50
        if(sale>=0)THEN
            mxnsale(4)=mxnsale(4)+1
        ELSE
            sale=sale+50
        end if
    end do
      end if
end do
 do i=1,4
    c%mxn(i)=c%mxn(i)-mxnsale(i)
    end do
    write(2,*)'Billetes MXN       $500        $200       $100        $50'
    write(2,*)'          ', c%mxn
    print*, '        $500        $200        $100         $50'
    print*,mxnsale
end select

End Program Cajero