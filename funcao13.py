import os
os.system('cls')

def confere():
    varL = 10 #VARIAVEL LOCAL
    print(f'Na função varL = {varL}')


confere()
print(f'na funcao: varL = {varL}')    
#erro, o escopo é so na função