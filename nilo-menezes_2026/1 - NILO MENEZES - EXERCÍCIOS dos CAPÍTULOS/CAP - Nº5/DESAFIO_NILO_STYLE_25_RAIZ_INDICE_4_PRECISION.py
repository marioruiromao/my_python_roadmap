# Exercício – Raiz de índice 4 usando o Método de Newton (CAP 5)

# Escreva um programa que:

# 1. Peça ao utilizador um número positivo.
# 2. Se o número for negativo, deve mostrar a mensagem:
#       "Número inválido. Digite apenas positivos."
#    e voltar a pedir outro número usando continue.
# 3. Quando o número for válido, deve sair do ciclo com break.
# 4. Use o método de Newton para calcular a raiz de índice 4 desse número.
#
# Regras obrigatórias:
# - usar while True para validar a entrada
# - usar continue para números inválidos
# - usar break quando o número é válido
# - usar b = n / 4 como chute inicial
# - usar precision = 0.000001
# - usar erro absoluto: abs(b*b*b*b - n)
# - atualizar b com a fórmula de Newton para raiz de índice 4:
#       b = (3*b + n/(b*b*b)) / 4
#
# No final, imprimir:
#       A raiz de índice 4 aproximada de X é Y
# com Y formatado para 6 casas decimais.

# ------------------------------------ RESOLUÇÃO: -----------------------------------------------
# SUPER NOTA: FÓRMULA GERAL DO MÉTODO DE NEWTON PARA RAIZ DE ÍNDICE k
# # b = ((k - 1)*b + n / (b**(k - 1))) / k

while True:
    n = float(input("Digite um número positivo para determinar a raiz de índice '4': "))

    if n < 0:
        print("Número inválido. Digite apenas positivos: ")
        continue
    
    break # neste caso se o número for positivo, saimos do DESTE ciclo,  e avançamos

b = n / 4       # É o nosso chute inicial. É uma forma de determinar um valor da melhor forma possível. b = n / k, em que k = índice da raiz |||
precision = 0.000001

while abs(b*b*b*b -n) > precision:      # É a fórmula do erro absoluto:  abs(b*b*b*b -n) em que o "b" repete-se "k" vezes!!!
    b = (3*b + n/(b*b*b)) / 4

print(f"A raiz de indice 4 aproximada ao valor {n} é de {b:.2f}")