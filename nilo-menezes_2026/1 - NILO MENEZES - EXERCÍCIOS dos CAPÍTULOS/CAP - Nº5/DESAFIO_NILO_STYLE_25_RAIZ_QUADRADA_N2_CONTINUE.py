# EXERCÍCIO 5.25 - VERSÃO 2
# Método de Newton para calcular a raiz quadrada por aproximação

while True:
    # Entrada do utilizador
    n = int(input('Digite um número "positivo" para obter a sua raiz quadrada. '
                  'Para parar o programa digite "999": '))
    
    b = 2  # valor inicial da aproximação

    # Condição de saída
    if n == 999:
        break

    # Impedir números negativos
    if n < 0:
        print("Número inválido. Digite apenas números positivos.")
        continue  # volta ao topo do ciclo e pede novo número

    # Método de Newton
    while abs(n - (b * b)) > 0.0001:
        p = (b + (n / b)) / 2
        b = p

    # Resultado final
    print(f"A raiz de {n} é por aproximação o valor {p:8.2f}")

# MUITO IMPORTANTE:
#   A ORDEM QUE TENHO SEMPRE QUE SEGUIR:

#       ✔ Fluxo de validação
#       ✔ Fluxo de cálculo
#       ✔ Fluxo de saída





