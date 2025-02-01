a = float(input("Digite os valores: "))
b = float(input("Digite os valores: "))
c = float(input("Digite os valores: "))
if a+b>c and a+c>b and b+c>a:
    print("Esses valores podem ser comprimentos de um triangulo.")
    if a==b==c:
        print("Triangulo equilátero.")
    elif a==b or b==c or a==c:
            print("Triangulo isósceles.")
    else:
        print("Triangulo escaleno.")
else:
    print("Esses valores não podem ser comprimentos de um triangulo.")