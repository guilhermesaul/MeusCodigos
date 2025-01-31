v = float(input("Velocidade do carro: "))
if v <= 50:
    print("Velocidade permitida")
elif v <= 55:
    print("Advertência")
elif v <= 65:
    print("Infração leve")
elif v <= 70:
    print("Infração média")
elif v <= 75:
    print("Infração grave")
else:
    print("Infração gravíssima")