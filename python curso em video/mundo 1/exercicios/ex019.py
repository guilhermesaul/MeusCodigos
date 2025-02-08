import random
e = input('Digite o nome de um aluno: ')
a = input('Digite o nome de um aluno: ')
l = input('Digite o nome de um aluno: ')
g = input('Digite o nome de um aluno: ')
r = (e, a, l, g)
escolha = random.choice(r)
print('A pessoa escolhida foi: {}'.format(escolha))
