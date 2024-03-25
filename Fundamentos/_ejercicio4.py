dni = input('Ingrese su DNI: ').strip()
edad = input('Ingrese su Edad: ').strip()



if not (dni and edad): 
    print('Usted no ha ingreso su DNI ,ni edad por lo tanto puede generar la cuenta')
else:
    edad = int(edad)
    if edad <= 12:
        print('No se puede crear una cuenta por su edad')
    elif 13 <= edad <= 17:
        print('Puedes tener una cuenta con control parental')
    else:
        print('Puede tener una cuenta con acceso total')

    
