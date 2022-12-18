## ejemplo de listas en python 

#Creando una lista
nombres = ["Paola", "Carlos", "Mario", "Israel", "Manuel", "Luis", "Guillermo"]

# Accediendo y pintando un elemento con x posicion de la lista
print(nombres[1])

# Cambiando un elemento con x posicion en la lista
nombres[0]="Elizabeth"

# Agregar elementos a la lista

nombres.insert(7, "Juan")
nombres.insert(1, "Pedrita")

nombres.append("Perenganita")
##nombres.("sutanita")

print(nombres)

# Despues de dos meses 

nombres.remove("Juan")


#Barrer una lista
#Para barrer una lista, se requiere un loop 
#FOR 
#WHILE 
#DO-WHILE
#FOREACH 


for x in nombres:
    print(x)



nombres.pop(1)

print(nombres)


for y in range(1):
    print(nombres[y])

print(len(nombres))


## WHILE 


i = 0 

while i < len(nombres):
    print(nombres[i])
    i = i + 1 



## Como comentamos previamente, las listas son estructuras de datos que son especiales 
## por lo que podemos utilizar con ellas diferentes metodos, por ejemplo ordenar

nombres = ["Paola", "Carlos", "Mario", "Israel", "Manuel", "Luis", "Elizabeth","Guillermo", "David"]
alfabetico = sorted(nombres.copy())
keys = sorted(nombres.copy() , key=len)
reversas = sorted(nombres.copy() , reverse=True)


## Imaginemos que debemos ordenar nuestra lista por orden ascendente 
#alfabetico.sort()
print(alfabetico)
print(keys)
##Mediante una llave especificado

#reversas.sort(key=len)
print(reversas)

## Mediante la variable reversa y su inicializacion en booleano (true en caso de que queramos que el acomodo sea en reversa)
# reverse false si no queremos


# nombres.sort(reverse= True)
# print(nombres)

# nombres.sort(key=len, reverse= True)
# print(nombres)



print("Se incribieron", nombres)





