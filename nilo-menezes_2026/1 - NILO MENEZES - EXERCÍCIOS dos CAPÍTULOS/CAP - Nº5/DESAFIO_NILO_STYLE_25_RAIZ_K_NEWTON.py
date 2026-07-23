# Exercício – Raiz de índice k usando Newton (versão robusta) – CAP 5

# Escreva um programa que:

# 1. Peça ao utilizador dois valores:
#       - n > 0
#       - k > 1

# 2. Se n <= 0 ou k <= 1:
#       - mostrar:
#             "Valores inválidos: digite n > 0 e k > 1."
#       - voltar ao início do ciclo usando continue

# 3. Quando ambos forem válidos, sair com break.

# 4. Definir:
#       b = n / k
#       precision = 0.000001
#       iteracoes = 0

# 5. Calcular a raiz de índice k de n usando Newton.

#    Utilizar:
#       erro absoluto: abs(b**k - n)

#    Atualizar b com a fórmula geral:
#       b = ((k - 1)*b + n / (b**(k - 1))) / k

# 6. Contar as iterações até o erro ficar menor que a precisão.

# 7. Imprimir:
#       A raiz de índice k aproximada de n é b
#       Número de iterações: X

#    com b formatado para 6 casas decimais.

# _____________________________________ RESOLUÇÃO _______________________________________

while True:
    n = float(input("Digite um valor maior que zero, para calcular a sua raiz: "))
    k = int(input("Escolha o índice da raiz. O valor tem que ser maior que um: "))

    if n <= 0 or k <= 1:
        print("Erro! Insira valores corretos.")
        continue
    break
b = n / k   # É o chute inicial
precision = 0.000001
iteracao = 0

# CICLO DO MÉTODO DE NEWTON
while abs(b**k - n) > precision:        # Este é o critério de paragem.
    b = ((k - 1)*b + n / (b**(k - 1))) / k
    iteracao += 1

print(f"A raiz de índice {k} do valor {n} é {b:.6f}")
print(f"Foram precisas {iteracao} iterações.")