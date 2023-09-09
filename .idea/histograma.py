positivos=0
negativos=0
print("ingrese valores entrero (0 para finalizar)")
while(True):
    x=int(input())
    if(x==0):
        break
    if(x>0):
        positivos +=1
    else:
        negativos +=1
print("valores positivos")
for _ in range(positivos):
    print("*", end=" ")
print(f" ")
print("valores negativos")
for _ in range(negativos):
    print("*" , end= " ")