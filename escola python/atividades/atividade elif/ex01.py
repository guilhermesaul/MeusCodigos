print("*"*65)
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("*"*65)
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("*"*65)
g = int(input("Qual grandeza deseja calcular? "))
if g == 1:
    r = float(input("Informe o valor da Resistência: "))
    c = float(input("Informe o valor da Corrente: "))
    t = r * c
    print(f"Tensão calculada: {t:.2f} V")
elif g == 2:
    t = float(input("Informe o valor da Tensão: "))
    c = float(input("Informe o valor da Corrente: "))
    r = t/c
    print(f"Resistência calculada: {r:.2f} Ω")

elif g == 3:
    t = float(input("Informe o valor da Tensão: "))
    r = float(input("Informe o valor da Resistência: "))
    c = t/r
    print(f"Corrente calculada: {c:.2f} A")

else:
    print("Opção inválida")