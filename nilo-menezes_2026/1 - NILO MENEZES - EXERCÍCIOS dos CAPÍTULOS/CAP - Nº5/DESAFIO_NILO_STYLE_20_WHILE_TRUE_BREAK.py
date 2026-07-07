
# EXERCÍCIO — Capítulo 5 (Nilo Menezes)
# ---------------------------------------------------------
# Lê vários números inteiros do utilizador.
# O programa deve terminar quando o utilizador digitar 0.
#
# Durante a leitura:
#   - Conta quantos números POSITIVOS foram digitados.
#   - Conta quantos números NEGATIVOS foram digitados.
#   - Soma apenas os números POSITIVOS.
#
# No final, o programa deve mostrar:
#   - Quantidade de números positivos
#   - Quantidade de números negativos
#   - Soma dos números positivos
#   - Média dos números positivos
#
# Observações:
#   - Usa while True e break.
#   - Usa acumuladores e contadores.
#   - Não usar listas, funções ou nada além do Capítulo 5.
# ---------------------------------------------------------

# RESOLUÇÃO:______________________________________________________________________________________


# EXERCÍCIO — Capítulo 5 (Nilo Menezes)
# ---------------------------------------------------------
# Lê vários números inteiros do utilizador.
# O programa deve terminar quando o utilizador digitar 0.
#
# Durante a leitura:
#   - Conta quantos números POSITIVOS foram digitados.
#   - Conta quantos números NEGATIVOS foram digitados.
#   - Soma apenas os números POSITIVOS.
#
# No final, o programa deve mostrar:
#   - Quantidade de números positivos
#   - Quantidade de números negativos
#   - Soma dos números positivos
#   - Média dos números positivos
# ---------------------------------------------------------

numeros_positivos = 0       # Contador → vai contar quantos números POSITIVOS foram digitados.
numeros_negativos = 0       # Contador → vai contar quantos números NEGATIVOS foram digitados.
soma = 0                    # Acumulador → vai somar APENAS os números positivos, que vou definir mais tarde

while True:                 # while True → laço infinito que só termina com break.
    numero = int(input('Digite todos os números que quiser - para parar digite zero (0): '))
    
    if numero == 0:         # Se for 0 → o utilizador quer parar.
        break

    if numero > 0:                  # Se o número for POSITIVO:
        numeros_positivos += 1      # Contador: aumenta 1 sempre que encontro um número positivo.
        soma += numero              # Acumulador: somo o valor do número positivo ao total.

    elif numero < 0:                # Se o número for NEGATIVO:
        numeros_negativos += 1      # Contador: aumenta 1 sempre que encontro um número negativo.

# Fim do while → já tenho quantidade de positivos, negativos e soma dos positivos.

if numeros_positivos > 0:
        # Só posso calcular média se houver pelo menos 1 número positivo.
        media = soma / numeros_positivos
else:
        media = 0
        # Evita divisão por zero.

print(f'Temos {numeros_positivos} números positivos!')
print(f'Temos {numeros_negativos} números negativos!')
print(f'A soma dos números positivos é: {soma}.')
print(f'A média dos números positivos é: {media}.')



                                 