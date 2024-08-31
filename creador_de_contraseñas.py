import random
letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = int(input("cual es la longitud de la contraseña"))
password_result = ""
for i in range (password):
    password_result += random.choice(letras)
print(password_result)
