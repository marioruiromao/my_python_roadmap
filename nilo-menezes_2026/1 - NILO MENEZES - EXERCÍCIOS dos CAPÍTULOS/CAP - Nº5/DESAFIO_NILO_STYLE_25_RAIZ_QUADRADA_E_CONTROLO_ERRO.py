# Exercício – Método de Newton para raiz quadrada com controlo de erro (CAP 5)
# Escreva um programa que:

# 1. Peça ao utilizador um número positivo n.
#
# 2. Se n for negativo ou igual a zero:
#       - mostrar a mensagem:
#             "Valor inválido. Digite apenas positivos."
#       - voltar ao início do ciclo usando continue
#
# 3. Quando n for válido, sair do ciclo com break.
#
# 4. Definir:
#       b = n / 2              # chute inicial
#       precision = 0.000001   # tolerância de erro
#
# 5. Calcular a raiz quadrada de n usando o método de Newton.
#
#    Utilizar:
#       erro absoluto: abs(b*b - n)
#
#    Atualizar b com a fórmula:
#       b = (b + n/b) / 2
#
# 6. Contar quantas iterações o ciclo executa até o erro ficar
#    menor que a precisão.
#
# 7. No final, imprimir:
#       A raiz quadrada aproximada de n é b
#       Número de iterações: X
#
#    com b formatado para 6 casas decimais.
#############################################################################
# Como um PROGRAMADOR experiente PENSA:
#   Antes de escrever código, um sénior pensa assim:
#  1 - Preciso de um ciclo para validar entrada.
#  2 - Depois preciso de outro ciclo para Newton.
#  3 - Cada ciclo tem o seu propósito.
#  4 - ABSOLUTAMENTE NADA do cálculo pode estar dentro do ciclo de validação.
#############################################################################
# Começamos por definir um CICLO para validar ENTRADA
while True:
    n = float(input("Introduza um valor positivo: "))

    if n <= 0: # O zero não tem raiz quadrada, é zero,é o único número cuja sua raiz é igual a ele próprio!
        print("Valor inválido. Digite apenas positivos.")
        continue
    break # Caso não haja erro, continuamos no nosso script.

b = n / 2                  # O nosso chute inicial. FORMULA GERAL: b = n / k, mas aqui estamos no caso especial k = 2.
precision = 0.000001       # O erro permitido
iteracoes = 0 

# Agora vamos definir o CICLO para o Método de Newton
while abs(b*b - n) > precision:      # Fórmula do erro absoluto: abs(b*b - n)
    b = (b + n / b) / 2 
    iteracoes += 1

print(f"A raiz quadrada e {n} é {b:6f}.")
print(f"O número de iterações foram {iteracoes}.")

#________________________________________________________________________________
# FÓRMULAS do MÉTODO DE NEWTON:

# PARA A RAIZ QUADRADA:     b = (b + n/b) / 2
#      PARA A RAIZ 'K':     b = ((k - 1)*b + n / (b**(k - 1))) / k
# _______________________________________________________________________________

# VERSÃO PYTHONIC

while True:
    n = float(input("Introduza um valor positivo: "))

    if n <= 0:
        print("Valor inválido. Digite apenas positivos.")
        continue

    break

b = n / 2
precision = 0.000001
iteracoes = 0

while abs(b*b - n) > precision:
    b = (b + n / b) / 2
    iteracoes += 1

print(f"A raiz quadrada de {n} é {b:.6f}.")
print(f"O número de iterações foi {iteracoes}.")
