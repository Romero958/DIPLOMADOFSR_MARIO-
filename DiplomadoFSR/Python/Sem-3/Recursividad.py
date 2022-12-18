## Repeticion 
## Auto llamado 
## Detener en un tiempo especifico


## Cuenta regresiva 

def cuenta_reg(num) : 
    num -= 1 
    if num > 0: 
        print(num)
        cuenta_reg(num)
    else:
        print("Termino el timer")


    print( f"Termino la funcion {num}")

cuenta_reg(3)

    
     
