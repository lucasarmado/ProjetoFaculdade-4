import os
os.system('cls')

def horaMinutoSegundo(hora):
    print(f'{hora} hora(s) trabalhadas são igual a {hora * 60} minutos e {hora*3600} segundos')
    print(f'O total de horas trabalhadas foi de {hora} horas')

hora = int(input('Digite as horas trabalhadas: '))

horaMinutoSegundo(hora)
