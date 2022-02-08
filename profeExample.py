from array import array
import random
arrayExample =[1,2,3,4,5]
for i in range(5):
    arrayExample[i]=int(random.uniform(100,200))

    varInput=int(input("ingrese valor: "))
    for i in range(5):
        if arrayExample[i]>=varInput:
            print("valor del arreglo mayor")
        else:
            print("valor del arreglo menor")
    print(arrayExample)
    