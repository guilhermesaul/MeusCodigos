f = float(input("Digite a temperatura em fahrenheit: "))
c = (f-32)*(5/9)
if c < 17:
    print("Está frio")
elif c < 25:
    print("Está agradável")
else:
    print("Está calor")