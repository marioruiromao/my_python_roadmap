# ------------------------------------------------------------
# DESAFIO COMPLETO: Calcular o MMC e analisar múltiplos de 1 a 200
# ------------------------------------------------------------

# Primeiro pedimos dois números ao utilizador. O input devolve texto,
# por isso usamos int() para converter para número inteiro.
a = int(input("Digite um número inteiro: "))
b = int(input("Digite um outro número inteiro: "))

# Guardamos os valores originais porque o cálculo do MMC vai alterar 'a' e 'b'.
a_original = a
b_original = b

# Agora vamos calcular o MMC usando fatoração simultânea.
# Começamos com mmc = 1 porque é o elemento neutro da multiplicação.
mmc = 1
divisor = 2  # Começamos pelo menor divisor útil.

# Enquanto pelo menos um dos números ainda for maior que 1,
# continuamos a tentar dividir pelos divisores.
while a > 1 or b > 1:

    # Se o divisor dividir pelo menos um dos números, ele faz parte do MMC.
    if a % divisor == 0 or b % divisor == 0:

        # Multiplicamos o MMC por esse divisor.
        mmc = mmc * divisor

        # Se 'a' for divisível, dividimos.
        if a % divisor == 0:
            a = a // divisor

        # Se 'b' for divisível, dividimos.
        if b % divisor == 0:
            b = b // divisor

    else:
        # Se o divisor não servir, passamos para o próximo número.
        divisor = divisor + 1

# Quando o ciclo termina, o MMC está calculado.
print("\nMMC =", mmc)
print("\n--- Iniciando análise de múltiplos de 1 a 200 ---\n")

# Agora vamos analisar cada número de 1 a 200.
# range(1, 201) gera os números de 1 até 200.
for n in range(1, 201):   # Range cria uma sequência de números que podes usar num ciclo 'for'. Ex. range(5) - o 5 não entra. Range(1, 201) - o 201 não entra.
    # Começamos a mensagem com o número atual.
    mensagem = f"{n}"

    # Se for múltiplo do primeiro número original:
    if n % a_original == 0:
        mensagem += " → Múltiplo de A" # Pega no valor atual de mensagem, soma " → Múltiplo de A", e guarda o resultado de volta em mensagem'.

    # Se for múltiplo do segundo número original:
    if n % b_original == 0:
        mensagem += " → Múltiplo de B"

    # Se for múltiplo do MMC:
    if n % mmc == 0:
        mensagem += " 🔥 Múltiplo comum (MMC)"

    # Mostramos a mensagem final para este número.
    print(mensagem)

# No fim, mostramos uma mensagem de conclusão.
print("\nAnálise concluída!")
