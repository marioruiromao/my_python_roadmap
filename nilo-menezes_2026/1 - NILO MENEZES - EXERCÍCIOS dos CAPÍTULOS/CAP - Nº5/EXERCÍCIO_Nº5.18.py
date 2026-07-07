
# PROGRAMA 5.1

valor = int(input('Digite o valor a pagar: '))

cedulas = 0
apagar = valor 
atual = 100

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cedula(s) de {atual}€')
        if apagar == 0:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
    


    
