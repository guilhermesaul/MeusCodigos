a = float(input("Digite a estatura da primeira pessoa: "))
b = float(input("Digite estatura da segunda pessoa: "))
c = float(input("Digite estatura da terceira pessoa "))
if a>=b and b>=c:
	print(f"{a} \n{b} \n{c}")
elif a>=c and c>=b:
	print(f"{a} \n{c} \n{b}")
elif b>=a and a>=c:
	print(f"{b} \n{a} \n{c}")
elif b>=c and c>=a:
	print(f"{b} \n{c} \n{a}")
elif c>=a and a>=b:
	print(f"{c} \n{a} \n{b}")
else:
	print(f"{a} \n{c} \n{b}")