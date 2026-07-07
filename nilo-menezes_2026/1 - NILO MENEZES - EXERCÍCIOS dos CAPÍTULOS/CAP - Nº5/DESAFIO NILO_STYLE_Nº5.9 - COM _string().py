valor = input('Diga o dividendo: ').strip() # NT - input() devolve uma string, e a .strip() funciona apenas em strings.
while valor == '':
    print('Erro: tem de digitar um número.')
    valor = input('Diga o dividendo: ').strip() # método de texto (string) usado para remover caracteres no início e no fim da string. Não mexe no meio do texto
dividendo = int(valor)

valor = input('Diga o divisor: ').strip()
while valor == '':
    print('Erro: tem de digitar um número.')
    valor = input('Diga o divisor: ').strip()
divisor = int(valor)

quociente = 0 # Zero porque não houve ainda subtração.
resto = dividendo #Porque ainda não subtraimos nada

while resto >= divisor: #caso contrário não conseguimos tirar mais 'divisor' ao'resto'

    resto -= divisor

    quociente += 1 # É o número de ciclos que vais acontecendo... Este valor avança
    # á medida que avançam os ciclos: 1º ciclo dá quociente = 1, 2º ciclo dá quociente = 2,
    # e assim sucessivamente.

print(f'A divisão de {dividendo} / {divisor} = {quociente} (Resto {resto})')
# Coloco fora do While para não aparecerem todos os valores!


#================================================================================
# OUTRA FORMA MAIS COMPACTA!
#================================================================================

valor = input('Digite um valor: ').strip()
dividendo = int(valor)

valor = input('Diga outro valor: ').strip()
divisor = int(valor)

quociente = 0
resto = dividendo

while resto >= divisor:
    resto = resto - divisor
    quociente += 1

print(f'{dividendo} / {divisor} = {quociente} (resto {resto})')
