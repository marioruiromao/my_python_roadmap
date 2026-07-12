
n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")

# NOTAS:
# Este programa calcula a raiz quadrada de um número usando o método de Newton-Raphson.
# A variável 'b' é o palpite inicial para a raiz quadrada.
# O loop continua até que a diferença entre o quadrado do palpite e o número seja menor que 0.00001.
# A variável 'p' é o novo palpite calculado em cada iteração.

# (b + (n / b)) / 2 é exatamente a fórmula de Newton para raiz quadrada.
# p guarda o novo valor
# b = p atualiza a aproximação: o próximo ciclo vai usar esse novo valor como base.


# round() - serve para arredondar números, e são definidas pelo segundo argumento da função.
#           round(valor, numero_de_casas)
#           EXEMPLO: round(3.14159, 2) retorna 3.14

# abs() - retorna o valor absoluto de um número, ou seja, remove o sinal negativo se houver.
#         EXEMPLO: abs(-5) retorna 5