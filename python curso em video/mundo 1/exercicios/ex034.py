salario = float(input("Digite o salário do funcionário: "))
if salario <= 1250:
    aumento = salario*1.15
else:
    aumento = salario*1.10
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.")