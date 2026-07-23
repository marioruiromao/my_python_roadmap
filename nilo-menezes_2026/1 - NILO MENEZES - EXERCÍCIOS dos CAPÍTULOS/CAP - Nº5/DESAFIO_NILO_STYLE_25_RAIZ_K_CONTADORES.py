# Exercício – Método de Newton com raiz de índice variável e controlo de erro (CAP 5)

# Escreva um programa que:

# 1. Peça ao utilizador dois valores:
#       - um número positivo n
#       - um índice de raiz positivo k
#
# 2. Se n ou k forem negativos ou iguais a zero:
#       - mostrar a mensagem:
#             "Valores inválidos. Digite apenas positivos."
#       - voltar ao início do ciclo usando continue
#
# 3. Quando ambos os valores forem válidos, sair do ciclo com break.
#
# 4. Definir:
#       b = n / k              # chute inicial
#       precision = 0.000001   # tolerância de erro
#
# 5. Calcular a raiz de índice k de n usando o método de Newton.
#
#    Utilizar:
#       erro absoluto: abs(b**k - n)
#
#    Atualizar b com a fórmula geral:
#       b = ((k - 1)*b + n / (b**(k - 1))) / k
#
# 6. Contar quantas iterações o ciclo de Newton executa até o erro ficar
#    menor que a precisão.
#
# 7. No final, imprimir:
#       A raiz de índice k aproximada de n é b
#       Número de iterações: X
#
#    com b formatado para 6 casas decimais.

# ------------------------------------------------ RESOLUÇÃO ------------------------------------------------
# Como um PROGRAMADOR experiente pensa:
#   Antes de escrever código, um sénior pensa assim:

#  1 - Preciso de um ciclo para validar entradas.
#  2 - Depois preciso de outro ciclo para Newton.
#  3 - Cada ciclo tem o seu propósito.
#  4 - ABSOLUTAMENTE NADA do cálculo pode estar dentro do ciclo de validação.

#Só depois escreve.

while True:
    n = float(input("Introduza um valor positivo, para calcular a raiz usando o Método de Newton: "))
    k = int(input("Introduza o índice da raiz. O valor tem que ser positivo: "))
    
    if n <= 0 or k <= 0:
        print("Valores inválidos. Digite apenas positivos.")
        continue   # Aqui volto ao topo porque os valores são inválidos

    break          # Aqui saio do ciclo de validação — tudo OK

# MUITO IMPORTANTE: O meu erro: eu tinha colocado estas linhas DEPOIS do break, onde nunca seriam executadas
b = n / k          # Aqui defino o chute inicial corretamente
precision = 0.000001    # Eu tinha escrito 'precison' e nunca usei a variável

iterations = 0     # Eu não estava a contar iterações — preciso desta variável

# O meu erro: eu tinha colocado 'b += 1', o que destrói o método de Newton
while abs(b**k - n) > precision:
    b = ((k - 1)*b + n / (b**(k - 1))) / k   # Atualização correta
    iterations += 1                          # Conto uma iteração

# O meu erro: eu estava a imprimir b como número de iterações
print(f"A raiz de índice {k} aproximada de {n} é {b:.6f}")
print(f"O número de iterações necessárias foi: {iterations}")
