import random
matriz=[]
filas = int(input("Introduce numero de filas: "))
columnas= int(input("Introduce numero de columnas: "))   
for i in range(filas):
    for j in range(columnas):
        matriz.append([0]*columnas)
    
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]= round(random.uniform(0,100),2)
    
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j],end="\t")
    print('\n')