persona = {
    'nombre' : 'Elsa Perez',
    'edad' : 34,
    'skills' : ['Python', 'Javascript'],
    'direccion' : {
        'calle' : 'La Rioja',
        'numero' : 123
    }

}

print(persona['skills'][1])
print(persona.get('dni', 'No tiene dni'))


persona['dni'] = 34444555

print(persona)

persona['skills'].append('Postgres')
print(persona)

persona.pop('edad')
print('edad')

print(persona.keys())
print(persona.values())
print(persona.items())
