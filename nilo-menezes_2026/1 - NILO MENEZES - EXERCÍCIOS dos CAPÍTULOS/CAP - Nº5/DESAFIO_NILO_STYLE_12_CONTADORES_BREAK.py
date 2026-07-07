# Enunciado:

# Pede ao utilizador notas (valores entre 0 e 20).

# O programa deve parar quando o utilizador escrever 0.

# No final, mostra:
#       O total das notas;
#       Quantas notas foram introduzidas;
#       A média das notas.


total_notas = 0
quantidade = 0

while True:
    nota = int(input('Digite uma nota entre 0 e 20 (0 para terminar): '))

    while nota < 0 or nota > 20: # validação
        print('Valor inválido! A nota deve estar entre 0 e 20.')
        nota = int(input('Digite novamente uma nota entre 0 e 20 (0 para terminar): '))

    if nota == 0:
        break

    total_notas = total_notas + nota
    quantidade = quantidade + 1

print(f'Total das notas: {total_notas}')
print(f'Quantidade de notas: {quantidade}')

if quantidade > 0:
    media = total_notas / quantidade
    print(f'Média: {media:.2f}')
else:
    print('Nenhuma nota foi introduzida.')

