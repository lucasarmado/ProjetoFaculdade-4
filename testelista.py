import os
os.system('cls')

horario = int(input('Digite o horario atual: '))

if (horario >= 0) and (horario < 12):
    print('BOM DIA')
elif (horario > 12) and (horario < 18):
    print('BOA TARDE')
else:
    print('BOA NOITE')     


     
   