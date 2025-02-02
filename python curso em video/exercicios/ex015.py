d = int(input('Quantos dias esse carro foi alugado? '))
k = float(input('Quantos km rodados? '))
p = (d*60) + (k*0.15)
print('O carro foi alugado por {} dias e rodaram {} kms. \no preço a pagar é de {:.2f}'.format(d, k, p))
