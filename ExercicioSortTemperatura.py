import os
os.system('cls')

def sort (array):
    for temp in range(0, len(array)):
        min_temp = temp
    
        for prox in range(temp + 1, len(array)):
            if array[prox] < array[min_temp]:
                min_temp = prox

        array[temp], array[min_temp] = array[min_temp], array[temp]

array = [30,20,15,25,12,40]
sort(array)
print(array)
print("A temperatura máxima foi de",array[5],"graus" " e a mínima foi de",array[0],"graus.")