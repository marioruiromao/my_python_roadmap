
# Exercício — Método de Newton (Estilo Exame de Engenharia Informática)

# Pretende-se que implemente, em Python, um algoritmo iterativo baseado no
# Método de Newton para determinar uma aproximação de uma raiz real da função:

#   f(x) = x^3 - 5x^2 + 2

# Cumpram-se obrigatoriamente as seguintes condições:

# 1. O valor inicial deve ser escolhido pelo estudante, justificando-se a sua
#   adequação através da análise prévia do comportamento da função.

# 2. O critério de paragem deve utilizar o erro absoluto entre aproximações
#  consecutivas.

# 3. O programa deve solicitar ao utilizador:
#       - o valor máximo admissível para o erro;
#      - o número máximo de iterações permitidas.

# 4. O algoritmo deve terminar quando:
#       - o erro absoluto seja inferior ao valor especificado;
#       - ou quando o número máximo de iterações seja atingido.

# 5. No final, devem ser apresentados:
#       - a aproximação obtida;
#       - o número de iterações realizadas;
#       - o erro absoluto da última iteração.

# É proibida a utilização de funções definidas pelo utilizador.
# Apenas são permitidas instruções básicas (atribuições, ciclos, condicionais).

# ________________________________ RESOLUÇÃO _________________________________

# Leitura dos dados
p = float(input("Indique o valor máximo para o erro: "))
iteracoes_maximas = int(input("Defina o número máximo de iterações possível: "))

# Valor inicial escolhido pelo estudante
x = 1

# Inicialização
iteracoes = 0
erro = p + 1   # garantir que entra no ciclo. 

# Ciclo de Newton
while erro > p and iteracoes < iteracoes_maximas: # Qual é o valor de erro antes da primeira iteração. Se não inicializares erro, o Python nem sabe se deve entrar no ciclo.

    x_antigo = x       # Guardar o valor anterior. 

    # Atualização de Newton
    x = x - (x_antigo**3 - 5*x_antigo**2 + 2) / (3*x_antigo**2 - 10*x_antigo)

    erro = abs(x - x_antigo)              # erro entre aproximações consecutivas

    iteracoes += 1                        # contador

# Resultados finais
print("A aproximação obtida foi:", x)
print("Número de iterações realizadas:", iteracoes)
print("Erro absoluto da última iteração:", erro)


# 