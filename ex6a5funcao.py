import os
os.system ('cls')

def fibo(x):
	resultado = 0
	if (x == 1):
		return 0
	elif (x == 2):
		return 1
	else:
		return fibo(x-1)+fibo(x-2)

n=int(input("Entre com o valor: "))
print(f"O {n}° termo da sequência é o número: {fibo(n)}")