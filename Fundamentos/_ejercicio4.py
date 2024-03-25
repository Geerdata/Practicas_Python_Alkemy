dni = input('Ingrese su DNI').strip()
edad = input('Ingrese su Edad').strip()


if not (dni or edad) : 
    print('Usted no ha ingreso su DNI ,ni edad por lo tanto puede generar la cuenta')
