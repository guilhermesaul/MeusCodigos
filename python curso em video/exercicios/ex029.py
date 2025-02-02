carro = float(input("Digite sua velocidade (em km/h): "))
if carro <= 80:
    print("Tenha um bom dia!")
else:
    multa = (carro - 80)*7
    print("Você foi multado!")
    print(f"Sua multa foi de: {multa:.2f}R$")