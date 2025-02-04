distancia = float(input("Digite a distância da viagem (em km/h): "))
if distancia <= 200:
    custo = distancia/2
    print(f"Sua viagem é de {distancia}km")
    print(f"O custo da sua passagem vai ser de R${custo:.2f}")
else:
    custo = distancia*0.45
    print(f"Sua viagem é de {distancia}km")
    print(f"O custo da sua passagem vai ser de R${custo:.2f}")