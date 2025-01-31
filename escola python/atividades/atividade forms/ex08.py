n = int(input("Digite seu ano de nascimento: "))
i = 2024-n
if i < 16:
    print("Você não pode votar e nem tirar a carteira de habilitação")
elif i < 18:
    print("Você pode votar")
else:
    print("Você pode votar e tirar a carteira de habilitação")