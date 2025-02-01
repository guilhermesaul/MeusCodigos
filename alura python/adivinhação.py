print("*"*40)
print("Bem vindo no jogo de Adivinhação!")
print("*"*40)
num_secreto = 42
chute = int(input("Digite o seu número: "))
print(f"Você digitou {chute}")
if num_secreto == chute:
    print("Você acertou")
else:
    print("Você errou")
print("Fim do jogo")