
# Exercício:

# Leia vários números inteiros digitados pelo utilizador.
# O programa deve parar quando o utilizador digitar -1.
# Considere apenas os números PARES digitados.
# No final, mostre:
# 1) Quantos números pares foram digitados
# 2) A soma desses números pares
# 3) A média dos números pares
# Se nenhum número par for digitado, a média deve ser 0.


#       RESOLUÇÃO:

soma = 0            # soma: acumulador que guarda a SOMA dos números pares digitados
                    # ACUMULADOR = variável que vai acumulando valores ao longo do programa

numero_pares = 0    # numero_pares: contador que guarda QUANTOS números pares foram digitados
                    # CONTADOR = variável que aumenta sempre de 1 em 1

while True:         # while True: laço infinito que só termina quando eu usar 'break'
    numero = int(input('Digite os números inteiros que desejar, quando quiser parar digite "-1": '))
    
    if numero == -1:        # verifico primeiro se o utilizador quer parar.
        break

    if numero % 2 == 0:     # numero % 2 == 0 → verifica se o número é PAR
        numero_pares += 1   # CONTADOR: aumenta 1 cada vez que encontro um número par, estou a conta-los(DÁ-ME A QUANTIDADE).
        soma += numero       # ACUMULADOR: soma o valor do número par ao total
                             # no meu código original eu tinha soma += 1, o que estava errado
                             # soma += numero é o correto para acumular valores

# fim do while: agora já tenho a soma total e a quantidade total

if numero_pares > 0:        # só posso calcular média se houver pelo menos 1 número par
    media = soma / numero_pares     # fórmula correta da média: soma dos valores / quantidade de valores
else:
    media = 0         # se não houver números pares, defino média como 0, evita erro de divisão por zero.

print(f'Quantidade de números pares: {numero_pares}')
print(f'Soma dos números pares: {soma}')
print(f'Média dos números pares: {media}')
