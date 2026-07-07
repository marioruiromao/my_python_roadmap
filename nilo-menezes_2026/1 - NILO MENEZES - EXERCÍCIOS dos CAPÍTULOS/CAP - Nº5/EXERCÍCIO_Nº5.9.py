# ==================================================================================
#PROB - Ler 2 números. Divisão inteira do 1º pelo 2º, assim como o resto da divisão.
# ==================================================================================

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

quociente = 0 # É o número de ciclos que se repete
x = dividendo # 

while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")
