
numero = int(input('Determinar a tabuáda do: '))

x = 1

while x <= 10:
    print(numero * x)
    x += 1
            # MTO IMPORTANTE:
            # É esta expressão que alimenta o 'while' 
            # Faz o contador avançar para o próximo número.
            # Sem isto, o ciclo nunca acabava.

# ===================================================
# SOLUÇÃO Nilo Menezes:
# ===================================================

n = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
    
    # MTO IMPORTANTE:
    
    # É esta expressão 'x = x + 1' que alimenta o 'while', e faz o contador
    # avançar para o próximo número. Sem isto, o ciclo nunca acabava.
