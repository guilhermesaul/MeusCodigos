a = str(input("Digite o nome do produto: "))
b = float(input("Digite o valor do produto: "))
c = float(input("Digite o percentual de desconto: "))
d = b*c/100
e = b-d
print(f"Nome do produto: {a}. \nValor do produto: R${b:.2f}. \nPercentual do desconto: {c}%. \nValor do desconto: R${d}. \nValor final do produto: R${e}")