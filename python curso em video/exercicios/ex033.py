num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica qual número é maior
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3
    
# Verifica qual número é menor
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
    
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")