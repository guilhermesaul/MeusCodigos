nome = str(input("Digite o seu nome completo: ")).strip()
#nome1 = nome.split()
print(f"Seu nome completo em maiúsculas: {nome.upper()}")
print(f"Seu nome completo em minúsculas: {nome.lower()}")
print(f"Seu nome completo tem: {len(nome) - nome.count(" ")} letras")
print(f"Seu primeiro nome tem: {nome.find(" ")} letras") 
#print(f"Seu primeiro nome tem: {len(nome1[0])} letras") mesma coisa da linha 6