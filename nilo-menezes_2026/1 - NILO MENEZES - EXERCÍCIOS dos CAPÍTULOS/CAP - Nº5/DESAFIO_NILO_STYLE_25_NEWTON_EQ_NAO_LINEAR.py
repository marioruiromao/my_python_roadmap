# Exercício – Resolver a equação x^3 - 2x - 5 = 0 usando Newton (CAP 5)

# Escreva um programa que:

# 1. Peça ao utilizador um chute inicial x.

# 2. Definir:
#       precision = 0.000001
#       iteracoes = 0

# 3. Aplicar o método de Newton para resolver:
#       f(x) = x^3 - 2x - 5

#    Utilizar:
#       erro absoluto: abs(f(x))

#    Atualizar x com:
#       x = x - (x^3 - 2x - 5) / (3*x^2 - 2)

# 4. Repetir até o erro ser menor que a precisão.

# 5. No final, imprimir:
#       A solução aproximada é x
#       Número de iterações: X

#    com x formatado para 6 casas decimais.

# ______________________________________ RESOLUÇÃO ______________________________________  
# Resolver a equação x^3 - 2x - 5 = 0 usando o Método de Newton
# CAPÍTULO 5 — Nilo Menezes (sem funções)

# 1. Validar o chute inicial
while True:
    x = float(input("Digite um valor para o chute inicial (ex: 2 ou 3): "))

    # Aqui aceitamos qualquer número real como chute inicial.
    # Não há restrições matemáticas fortes, mas valores perto da raiz aceleram o método.
    break

# 2. Definir precisão e contador
precision = 0.000001
iteracao = 0

# 3. Método de Newton
# Fórmula geral:
# x_novo = x - f(x) / f'(x) NOTA: Não me posso esquecer de derivar a função no denominador!!!
#
# Para esta equação:
# f(x)  = x^3 - 2x - 5
# f'(x) = 3x^2 - 2
#
# Logo:
# x = x - (x^3 - 2x - 5) / (3*x^2 - 2)

while abs(x**3 - 2*x - 5) > precision:
    x = x - (x**3 - 2*x - 5) / (3*x**2 - 2)
    iteracao += 1

# 4. Resultado
print(f"A solução aproximada é {x:.6f}")
print(f"Foram necessárias {iteracao} iterações.")


#_______________________________________________________________
# MUITO IMPORTANTE:

# Fórmula geral do "Método de Newton": x_novo = x - f(x) / f'(x)
# ______________________________________________________________