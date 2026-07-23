# Exercício – Raiz cúbica usando o Método de Newton (CAP 5)

# Escreva um programa que:

# 1. Peça ao utilizador um número positivo n.

# 2. Se n <= 0:
#       - mostrar a mensagem:
#             "Valor inválido. Digite apenas positivos."
#       - voltar ao início do ciclo usando continue

# 3. Quando n for válido, sair do ciclo com break.

# 4. Definir:
#       b = n / 3              # chute inicial
#       precision = 0.000001   # tolerância de erro

# 5. Calcular a raiz cúbica de n usando o método de Newton.

#    Utilizar:
#       erro absoluto: abs(b**3 - n)

#    Atualizar b com a fórmula:
#       b = (2*b + n/(b*b)) / 3

# 6. Contar quantas iterações o ciclo executa até o erro ficar menor que a precisão.

# 7. No final, imprimir:
#       A raiz cúbica aproximada de n é b
#       Número de iterações: X

#    com b formatado para 6 casas decimais.
# ____________________________ RESOLUÇÃO ___________________________

# Começamos por definir um CICLO para validar ENTRADA
# “Primeiro valido entrada.
# Depois inicializo variáveis.

while True:
    n = float(input("Digite um número para calcular a sua raiz cúbica:  "))

    if n <= 0: 
        print("Valor inválido! Só são aceites valores positivos.")
        continue
    break

b = n / 3               # # Chute inicial correto para raiz cúbica.
precision = 0.000001    # É a tolerância do erro.
iteracao = 0

# Agora vamos definir o CICLO para o Método de Newton

while abs(b**3 - n) > precision:    # Erro absoluto: abs(b**k - n)
    b = (2*b + n / b**2) / 3        # Método da Newton para a raiz cúbica
    iteracao += 1                   # Contador de iterações.

# Depois saída formatada.
# Cada bloco tem o seu propósito.
# Nunca misturo blocos.

print(f"A raiz cúbica de {n} é {b:.6f}")
print(f"Foram necessárias {iteracao} iterações.")

#________________________________________________________________________________
# FÓRMULAS do MÉTODO DE NEWTON:

# PARA A RAIZ QUADRADA:     b = (b + n/b) / 2
#      PARA A RAIZ 'K':     b = ((k - 1)*b + n / (b**(k - 1))) / k
# _______________________________________________________________________________

# Como um sénior abordaria antes de escrever código

# Um programador experiente pensa assim:

# “Primeiro valido entrada.
# Depois inicializo variáveis.
# Depois Newton.
# Depois saída formatada.
# Cada bloco tem o seu propósito.
# Nunca misturo blocos.”