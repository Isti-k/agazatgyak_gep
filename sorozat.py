import random

lista=[]

def feladat1():
    for i in range(15):
        szam=random.randint(-90,500)
        lista.append(szam)
        if i <14:
            print(szam,end="*")
        else:
            print(szam,end="")    

def oszthatoak_szama():
    szamlalo=0
    for i in range(0,len(lista),1):
        if lista[i] % 10==0:
            szamlalo+=1
        i+=1
    print(f"A tízzel osztható számok összege:{szamlalo}")
    
    return szamlalo








