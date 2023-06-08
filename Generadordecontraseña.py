import random
import string
import os 

print("Password: ")
while True:
    lower= string.ascii_lowercase
    upper= string.ascii_uppercase
    num= string.digits
    symbols=string.punctuation
    chars= lower+upper+num+symbols
    temp= random.sample(chars,25)
    print("".join(temp))
    os.system("pause")
    print("¿Desea seguir?")
    print("1- si")
    print("2- no")
    opcion=int(input("Ingrese opcion: "))
    if opcion==1:
        print("")
    elif opcion==2:
        break