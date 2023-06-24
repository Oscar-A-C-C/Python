import random

letras= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros="123456789"
simbolos="{}´+!#$%&&/()=?'¿"

unir = f'{letras}{numeros}{simbolos}'
longitud=10
contraseña=random.sample(unir,longitud)
paswordfinal="".join(contraseña)

print(paswordfinal)