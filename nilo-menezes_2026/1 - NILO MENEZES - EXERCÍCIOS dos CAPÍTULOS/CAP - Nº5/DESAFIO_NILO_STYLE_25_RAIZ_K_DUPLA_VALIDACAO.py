# Exercício Avançado – Método de Newton para raiz de índice k (CAP 5)

# Escreva um programa que:

# 1. Peça ao utilizador dois valores:
#       - um número positivo n
#       - um índice de raiz positivo k

# 2. Se n <= 0 ou k <= 1:
#       - mostrar a mensagem:
#             "Valores inválidos. Digite n > 0 e k > 1."
#       - voltar ao início do ciclo usando continue

# 3. Quando ambos os valores forem válidos, sair do ciclo com break.

# 4. Definir:
#       b = n / k              # chute inicial
#       precision = 0.000001   # tolerância de erro
#       iteracoes = 0          # contador

# 5. Calcular a raiz de índice k de n usando o método de Newton.

#    Utilizar:
#       erro absoluto: abs(b**k - n)

#    Atualizar b com a fórmula geral:
#       b = ((k - 1)*b + n / (b**(k - 1))) / k

# 6. Contar quantas iterações o ciclo executa até o erro ficar
#    menor que a precisão.

# 7. No final, imprimir:
#       A raiz de índice k aproximada de n é b
#       Número de iterações: X

#    com b formatado para 6 casas decimais.

# ___________________________ RESOLUÇÃO ___________________________

# Preciso de um ciclo para validar entradas.
while True:
    n = float(input("Digite o valor 'n' positivo, para calcular a sua raiz, segundo o Método de Newton: "))
    k = int(input("Indique um valor 'k' maior que 1, para o índice da raiz: "))

    # Eu verifiquei se n <= 0 ou k <= 1. Isto garante que só aceito n > 0 e k > 1.
    if n <= 0 or k <= 1:
        print("Valores inválidos: digite n > 0 e k > 1.")
        continue
    # Se cheguei aqui, os valores são válidos e posso sair do ciclo.
    break
# Aqui defino o chute inicial. Para raiz de índice k, b = n / k é uma escolha razoável.
b = n / k
# Aqui defino a tolerância de erro. Este valor controla quando paro o método de Newton.
precision = 0.000001
# Contador de iterações. Vou incrementá-lo dentro do ciclo.
iteracao = 0

# Agora vou definir o CICLO para o Método de Newton.
# A condição usa o erro absoluto: abs(b**k - n) > precision.
while abs(b**k - n) > precision:
    # A fórmula abaixo é a fórmula geral de Newton para raiz de índice k.
    b = ((k - 1)*b + n / (b**(k - 1))) / k
    iteracao += 1

print(f"A raiz de índice {k} de {n} é {b:.6f}")
print(f"O número de iterações foi: {iteracao}.")




