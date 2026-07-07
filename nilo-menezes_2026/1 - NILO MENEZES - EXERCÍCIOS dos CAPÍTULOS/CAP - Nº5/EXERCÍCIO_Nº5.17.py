
# PROGRAMA 5.1

valor = int(input('Digite o valor a pagar: '))

cedulas = 0
apagar = valor 
atual = 50

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cedula(s) de {atual}€')
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        if atual == 20:
            atual = 10
        if atual == 10:
            atual = 5
        if atual == 5:
            atual = 1
        cedulas = 0
    
# RESPOSTA: O programa para imediatamente!

    
