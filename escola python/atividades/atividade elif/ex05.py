a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = b**2-4*a*c
if a != 0:
	if a > 0 and d > 0:
		print("Concavidade para cima e 2 raízes reais distintas (toca no eixo x em 2 pontos)")
	elif a > 0 and d == 0:
		print("Concavidade para cima e 2 raízes reais e iguais (toca no eixo x em 1 ponto)")
	elif a > 0 and d < 0:
		print("Concavidade para cima e não tem raiz real (não toca no eixo x)")
	elif a < 0 and d > 0:
		print("Concavidade para baixo e 2 raízes reais distintas (toca no eixo x em 2 pontos)")
	elif a < 0 and d == 0:
		print("Concavidade para baixo e 2 raízes reais e iguais (toca no eixo x em 1 ponto)")
	else:
		print("Concavidade para baixo e não tem raiz real (não toca no eixo x)")
else:
	print("Não é possível")