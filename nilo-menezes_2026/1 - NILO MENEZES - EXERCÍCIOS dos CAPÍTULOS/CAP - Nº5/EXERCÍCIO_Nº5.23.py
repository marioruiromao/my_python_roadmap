#  EXERCÍCIO 5.23

# SUPER DICA: 
#               1ª) Começar sempre primeiro por tratar os casos especiais, 
#               2º) depois o caso geral.


numero = int(input('Digite um número para verificar se é número primo: '))

# 1. Primeiro tratamos números negativos
if numero < 0:
    print('Erro! Digite só números inteiros positivos.')

# 2. Depois tratamos os casos especiais 0 e 1
elif numero == 0 or numero == 1:
    print(f"O número {numero} pertence aos casos especiais de números primos!")

# 3. Caso especial: 2 é primo. É O ÚNICO NÚMERO PAR QUE É PRIMO!
elif numero == 2:
    print("O número 2 é primo!")

# 4. Se for par e maior que 2 → não é primo
elif numero % 2 == 0:  # LÊ-SE: O resto da divisão de numero por 2 é igual a zero.
    print(f"Então {numero} não é número primo")

# 5. CASO GERAL: testar divisores ímpares
else:
    x = 3

    # Testamos apenas números ímpares até chegar ao próprio número
    while x < numero:
        if numero % x == 0:
            break
        x = x + 2   # É assim que avançamos para o próximo ímpar.

    # Se chegámos ao número sem encontrar divisores → é primo
    if x == numero:
        print(f'O {numero} é número primo')
    else:
        print(f"O {numero} não é primo!")




# QUANDO USAR 'WHILE TRUE' ou apenas 'WHILE'?
# ------------------------------------------------------------
#
# 1) O 'while' controla a tabuada entre dois limites:
#       - while inicio <= fim
#       - Isto é um loop com limite conhecido. 
#       - Quando o número de repetições é conhecido.

# 2) "while True" só deve ser usado quando:
#       - o número de repetições é desconhecido
#       - existe um "break" claro dentro do loop

# OUTRA NOTA: O plano geral (o “truque” matemático)

# Para saber se um número é primo, a ideia é:
# 1 - tentar dividir esse número por outros números menores que ele,    
#     se algum deles dividir “certinho” (resto 0), então não é primo
# 2 - se nenhum deles dividir certinho, então é primo.
# 3 - Aqui, como já trataste os pares antes, só testas ímpares: 3, 5, 7, 9, …