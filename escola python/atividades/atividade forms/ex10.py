p = int(input("Quantos pães franceses foram vendidos hoje? "))
b = int(input("Quantas broas foram vendidas hoje? "))
b1 = b*1.5
p1 = p*0.6
t = p1+b1
g = t*0.1
print(f"Foram vendidos {p} pães franceses e {b} broas hoje. Arrecadando R${p1} na venda dos pães, R${b1} na venda das broas, totalizando R${t}. Logo, ele deve guardar R${g} na poupança.")