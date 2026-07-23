# Raiz cúbica usando o Método de Newton

while True:
    n = float(input("Digite um número positivo: "))

    if n < 0:
        print("Número inválido. Digite apenas positivos.")
        continue        # Se o número for negativo → imprime a mensagem → continue → volta ao topo → pede novo número

    break # Se o número for positivo → break → sai do ciclo e continua, ao contrário do exit().

b = n / 3   # chute inicial (b = n / k). O chute só precisa de ser: O chute inicial (initial_guess) é apenas um ponto de partida para Newton começar 
            # a aproximar-se da raiz. Ele não precisa de ser perfeito. Ele só precisa ser: positivo, não ser zero, razoável e simples de calcular.
precision = 0.000001

while abs(b*b*b - n) > precision:
    b = (2*b + n/(b*b)) / 3   # fórmula de Newton para raiz cúbica

print(f"A raiz cúbica aproximada de {n} é {b:.6f}")


############################################################# NOTAS IMPORTANTES  ################################################################

# "BREAK"
# Quando o Python encontra break: sai do while, continua o código logo abaixo do ciclo. Ou seja:
# 1) O programa continua. 2) Só o ciclo termina.

# "EXIT()"
# O que faz o exit()? O exit() é muito mais forte. Ele: termina o programa, fecha tudo, não executa mais nenhuma linha, não volta ao ciclo!

# NBH:
# O break só pára o ciclo.
# O exit pára o programa.
# Se o ciclo é a última coisa no programa, o break parece que pára tudo, mas não é o break que pára, é o fim do código.

# precision        - tolerância de erro; valor máximo de erro permitido
# tolerance        - outro nome para tolerância de erro, comum em engenharia
# error            - diferença entre o valor aproximado e o valor real
# approximation    - valor aproximado atual (ex.: b)
# initial_guess    - valor inicial escolhido para começar o método de Newton
# iteration        - cada volta do ciclo while
# converge         - aproximar-se da solução
# convergence      - processo de aproximação da solução
# threshold        - limite que decide quando parar o cálculo
# absolute_error   - erro absoluto: abs(b*b - n)
# max_error        - erro máximo permitido (igual ao precision)
