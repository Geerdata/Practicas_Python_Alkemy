def verificar_calificacion(nota1, nota2, nota3):
        promedio = (nota1 +  nota2 + nota3) / 3

        if promedio >= 6:
            return "APROBADO"
        else:
            return "REPROBADO"
  
print(verificar_calificacion(8,6,8))


