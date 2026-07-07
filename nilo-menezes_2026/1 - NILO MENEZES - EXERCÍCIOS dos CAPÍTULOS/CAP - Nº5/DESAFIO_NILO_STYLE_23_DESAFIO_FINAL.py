# Nível 3 — O Desafio Final (Capítulo 5)

# Lê vários números inteiros.
# O programa termina quando o utilizador digitar 999.
#
# Durante a leitura:
#   - Conta quantos números PARES foram digitados (CONTADOR)
#   - Soma apenas os números ÍMPARES (ACUMULADOR)
#   - Conta quantos números maiores que 100 foram digitados (OUTRO CONTADOR)
#
# No final, mostra:
#   - Quantidade de pares
#   - Soma dos ímpares
#   - Quantidade de números > 100

numeros_pares = 0
# CONTADOR → conta quantos números PARES foram digitados.

soma_impares = 0
# ACUMULADOR → soma apenas os números ÍMPARES.

numeros_maiores_100 = 0
# CONTADOR → conta quantos números maiores que 100 foram digitados.

while True:
    numeros = int(input('Digite números inteiros (999 para parar): '))
    # Leio um número inteiro do utilizador.

    if numeros == 999:
        # 999 é o sinal para terminar o programa.
        break

    if numeros % 2 == 0:
        # Se o número for PAR:
        numeros_pares += 1
        # Aumento o contador de pares.

    else:
        # Se não é par, então é ÍMPAR:
        soma_impares += numeros
        # Somo o número ímpar ao acumulador de ímpares.

    if numeros > 100:
        # Esta condição é independente das anteriores.
        # Um número pode ser par E > 100, ou ímpar E > 100.
        numeros_maiores_100 += 1
        # Conto quantos números são maiores que 100.

# Fim do while → já tenho:
# - quantidade de pares
# - soma dos ímpares
# - quantidade de números > 100

print(f'Quantidade de números pares: {numeros_pares}')
print(f'Soma dos números ímpares: {soma_impares}')
print(f'Quantidade de números maiores que 100: {numeros_maiores_100}')


# SUPER NOTAS - 
# 
# 1 - Para EDEFINIRMOS os números IMPARES PODEMOS FAZER: ( if numero %2 != 0 ) ou ( if numero % 2 == 1: )

# 2 - Porque NÃO posso usar "elif" neste exercício? Porque "elif" significa: “Se esta condição for verdadeira, ignora todas as outras.”. E isso destrói o exercício.
#     E neste programa à condições que NÃO são mutuamente exclusivas. Portanto, NÃO posso usar elif. Posso ter um nº maior que 100 e impar ao mesmo tempo, por exemplo.