import os
os.system("cls") 
import time

with open("dadosAPS.csv", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
dicionario = {}


for c in range(29):
	dicionario[c] = linhas[c+3].replace("\n","").replace(";","").split(',')

n = len(dicionario)
for j in range(n-1):
    for i in range (n-1):
        if dicionario[i] > dicionario[i+1]:
            aux = dicionario[i]
            dicionario[i] = dicionario[i+1]
            dicionario[i+1] = aux        
print("  ")
print("Gerando e salvando o arquivo...")
time.sleep(2.5)
print("Aguarde mais um momento..." + "\n")
time.sleep(3.0)

with open("ArquivoFinal.csv", "w") as arquivoFinal:
    arquivoFinal.write(linhas[0])
    arquivoFinal.write(linhas[1])
    arquivoFinal.write(str(linhas[2]).replace("''", ""))
    for n, af in dicionario.items():
        result = str(af)
        arquivoFinal.write(str(result).replace('[','').replace(']','') + "\n")

print("Arquivo salvo e pronto para uso!")
print("Verifique a pasta onde esta localizado o algoritmo.")




 