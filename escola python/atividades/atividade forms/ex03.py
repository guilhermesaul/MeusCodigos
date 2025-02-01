h = float(input("Digite a altura da parede: "))
p1 = float(input("Digite a largura da primeira parede: "))
p2 = float(input("Digite a largura da segunda parede: "))
ap1 = 2*(p1*h)
ap2 = 2*(p2*h)
at = p1*p2
asoma = ap1+ap2+at
l = asoma/12
print(f"Soma total das paredes e do teto: {asoma:.2f} m².")
print(f"Quantidade de latas de tinta necessárias: {l:.2f}.")