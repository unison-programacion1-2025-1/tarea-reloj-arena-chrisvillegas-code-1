# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir    
    if m<=0:
        print("Error: La altura debe ser un entero positivo")
        return
    else:
        for i in range(m, 0, -1):
            for j in range(m - i):
                print(" ", end="")
            for j in range(2 * i - 1):
                print(s, end="")
            print()
        for i in range(1,m):
            for j in range(m-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print(s,end="")
            print()
    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    pass
