
# Nível 5 — O Mestre dos Números (Capítulo 5)

# Lê vários números inteiros.
# O programa termina quando o utilizador digitar -1.
#
# Durante a leitura:
#   - Conta quantos números NEGATIVOS foram digitados (CONTADOR)
#   - Soma apenas os números PARES (ACUMULADOR)
#   - Conta quantos números estão entre 10 e 50 (OUTRO CONTADOR)
#   - Soma quantos números são múltiplos de 7 (OUTRO ACUMULADOR)
#
# No final, mostra:
#   - Quantidade de números negativos
#   - Soma dos números pares
#   - Quantidade de números entre 10 e 50
#   - Soma dos números múltiplos de 7


# RESOLUÇÃO:

numeros_negativos = 0       #contador
soma_pares = 0           #acumulador
entre_10_e_50 = 0           #contador
multiplos_7 = 0             #acumulador

while True:
    numeros = int(input('Digite os números que quiser! Para terminar digite"-1": '))
    if numeros == -1:
        break

    if numeros < 0:
        numeros_negativos += 1
    if numeros %2 == 0:
        soma_pares += numeros
    if 10 < numeros < 50:
        entre_10_e_50 += 1
    if numeros %7 == 0:
        multiplos_7 += numeros

print(f'Números negativos: {numeros_negativos}')
print(f'A soma dos pares é: {soma_pares}')
print(f'Os Valores entre 10 e 50 são: {entre_10_e_50}')
print(f'Os multiplos de 7 são: {multiplos_7}')



# SUPER NOTA - COMO UM PROGRAMADOR PENSA ESTE CÓDIGO?

# Um programador experiente olha para isto e pensa:
# ✔️ “As condições são independentes?” SIM.
# Um número pode ser:
#   Negativo e par
#   Par e múltiplo de 7
#   Entre 10 e 50 e múltiplo de 7
#   etc.
# Logo: 👉 if independentes é a escolha certa.
