# EXERCÍCIO 5.26

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Agora, o divisor: "))
quociente = 0
x = dividendo

while x >= divisor:
    x = x - divisor
    quociente = quociente + 1

resto = x

print(f"O resto de {dividendo} / {divisor} = {resto}")