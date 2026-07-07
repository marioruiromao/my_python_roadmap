# =====================Enunciado==========================================================================

# Cria um programa que registe temperaturas diárias.

# O programa deve:

# Pedir ao utilizador uma temperatura (entre –30 e 50 graus).

# O programa deve parar quando o utilizador escrever 129.

# Antes de aceitar cada temperatura, o programa deve validar se está dentro do
# intervalo permitido (–30 a 50).

# No final, o programa deve mostrar:

#       1 - O total de temperaturas registadas
#       2 - A soma de todas as temperaturas
#       3 - A temperatura média
#       4 - A temperatura mais alta
#       5 - A temperatura mais baixa

#===========================================================================================================

# Inicialização dos acumuladores
soma = 0
quantidade = 0
primeira = True

while True:  # Usa um while dentro de outro quando tens um processo que
             # precisa de repetir sozinho, sem avançar o programa.

    # CICLO DE LEITURA E VALIDAÇÃO
    while True:
        temperatura = int(input('Digite uma temperatura entre -30 e 50 (129 para terminar): '))

        if temperatura == 129:
            break  # sai do ciclo de leitura

        if temperatura < -30 or temperatura > 50:
            print('Erro! Temperatura fora do intervalo.')
            continue  # volta ao início do ciclo de leitura

        break  # temperatura válida → sai do ciclo de leitura

    # SE FOR 129 → break geral
    if temperatura == 129:
        break

    # PRIMEIRA TEMPERATURA
    if primeira:
        maior = temperatura
        menor = temperatura
        primeira = False

    # ACUMULADORES
    soma += temperatura
    quantidade += 1

    # MAIOR E MENOR
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

# RESULTADOS
print(f'\nTotal de temperaturas registadas: {quantidade}')
print(f'Soma das temperaturas: {soma}')

if quantidade > 0:
    media = soma / quantidade
    print(f'Média das temperaturas: {media:.2f}')
    print(f'Temperatura mais alta: {maior}')
    print(f'Temperatura mais baixa: {menor}')
else:
    print('Nenhuma temperatura válida foi registada.')

# NOTA:
# O QUE É UM ACUMULADOR? Um acumulador é uma variável que vai somando valores ao longo do tempo.
# É como um mealheiro: cada moeda que colocas → aumenta o total, mas o mealheiro mantém o valor anterior
# e adiciona o novo valor por cima

