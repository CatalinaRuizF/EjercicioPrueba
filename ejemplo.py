from email.errors import NonPrintableDefect
import random
arrayRandom = [1,2,3,4,5]

for i in range(5):
    print(arrayRandom[i])
    arrayRandom[i]=(random.randrange(-100,100))
    print ("-------------------------------")
    print(arrayRandom[i-1])
