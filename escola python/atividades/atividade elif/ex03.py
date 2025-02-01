a = float(input("Digite um número positivo: "))
b = float(input("Digite um segundo número positivo: "))
print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")
c = int(input("Escolha uma opção: "))
if c==1:
	r = (a*0,2)+(b*0,3)
	print(f"A média ponderada é: {r}")
elif c==2:
	s = a+b
	q = s*s
	print(f"O quadrado da soma dos 2 números é: {q}")
elif c==3 and a>b:
	cu = b**3
	print(f"Cubo do menor número: {cu}")
elif c==3 and b>a:
	cu = a**3
	print(f"Cubo do menor número: {cu}")
else:
	print("Opção inválida")