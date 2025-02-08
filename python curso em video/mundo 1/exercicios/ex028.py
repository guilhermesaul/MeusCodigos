from random import randint
from time import sleep
computador = randint(0, 5)
chute = int(input("Digite um número entre 0 a 5: "))
print("Pensando...")
sleep(3)
if chute == computador:
    print("Parábens, você acertou!")
else:
    print("Você errou.")
print(f"Eu pensei no número {computador} e você chutou o número {chute}.")