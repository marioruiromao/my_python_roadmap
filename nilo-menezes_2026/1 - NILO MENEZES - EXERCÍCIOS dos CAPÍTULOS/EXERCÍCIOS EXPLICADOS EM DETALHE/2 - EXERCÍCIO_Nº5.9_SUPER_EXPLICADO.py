# ==================================================================================
#PROB - Ler 2 números. Divisão inteira do 1º pelo 2º, assim como o resto da divisão.
# ==================================================================================


dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

# O quociente começa em 0.
# Sempre que conseguirmos subtrair o divisor ao dividendo, significa que cabe mais 1 vez.
quociente = 0

# A variável x começa igual ao dividendo. Vamos "gastar" este valor subtraindo o divisor repetidamente.
x = dividendo

# Enquanto ainda for possível subtrair o divisor ao valor atual x (dividendo), continuamos a dividir.
while x >= divisor:

    # Subtraímos o divisor ao valor atual, isto simula uma divisão através de subtrações sucessivas.
    x = x - divisor

    # Cada subtração significa que o divisor coube mais uma vez.
    quociente = quociente + 1 #(quociente += 1))

# Quando o ciclo termina, x já não é grande o suficiente para subtrair o divisor, por isso 'x é o resto da divisão.
resto = x

# Mostramos o resultado final:
# - quociente: quantas vezes o divisor coube no dividendo
# - resto: o que sobrou
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")


# NBH - Para dividir, subtrair o divisor ao dividendo, até não ser possível mais.
#       Contar quantas subtrações fizeste → quociente.
#       O que sobrar → resto.
