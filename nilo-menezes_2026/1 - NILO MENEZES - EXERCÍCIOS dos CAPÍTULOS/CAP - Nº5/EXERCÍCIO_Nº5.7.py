


inicio = int(input("Digite o PRIMEIRO número da tabuáda: "))
fim = int(input('Digite o ÚLTIMO número da tabuáda: '))

while inicio <= fim:
    print(f"{inicio} x {fim} = {inicio * fim}")
    inicio = inicio + 1



# NILO MENEZES STYLE: ======================================

n = int(input("Tabuada de: "))

inicio = int(input("De: "))
fim = int(input("Até: "))

x = inicio

while x <= fim:
    print(f"{n} x {x} = {n * x}")
    x = x + 1


    
# NOTA SUPER IMPORTANTE: O papel de cada variável:

# 1) inicio → é o valor onde a tabuada começa
# 2) fim → é o valor onde a tabuada termina
# 3) x → é o contador, o “marcador” que anda de inicio até fim

# Pensa assim: inicio e fim são como marcas fixas numa régua.
# x é o dedo que se move da marca inicio até à marca fim.
# As marcas não mudam, o que muda é o dedo é que se mexe.
