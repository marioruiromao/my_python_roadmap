# ============================================================
# ENUNCIADO — Método de Newton (formato de teste universitário)
# ============================================================
#
# Pretende-se que escreva um programa em Python que determine uma
# aproximação para a raiz cúbica de um número real positivo, usando
# o Método de Newton.
#
# O programa deve cumprir obrigatoriamente os seguintes requisitos:
#
# 1. Solicitar ao utilizador um valor real n, garantindo que n > 0.
#    Caso contrário, o programa deve emitir uma mensagem de erro e
#    repetir a leitura até obter um valor válido.
#
# 2. Utilizar como valor inicial de aproximação o resultado de n
#    dividido por 3.
#
# 3. Utilizar uma tolerância fixa igual a 0.000001.
#
# 4. Implementar um ciclo que continue enquanto o erro absoluto entre
#    a aproximação atual e o valor pretendido for superior à tolerância.
#
# 5. Em cada iteração, atualizar a aproximação segundo o procedimento
#    do Método de Newton aplicado ao cálculo da raiz cúbica.
#
# 6. No final, o programa deve apresentar:
#       - a aproximação obtida, com seis casas decimais;
#       - o número total de iterações realizadas.
#
# ============================RESOLUÇÃO================================

while True:
    n = float(input("Digite um valor maior que zero para determinar a sua raiz cúbica: "))

    if n <= 0:
        print("Erro! O valor deve ser maior que zero.")
        continue
    break

b = n / 3   
precision = 0.000001
iteracao = 0

# Calculo do erro absoluto
while abs(b**3-n) > precision:
    b = (2*b + n / (b**2)) / 3
    iteracao += 1

print(f"A raiz cúbica de {n} é {b:.6f}")
print(f"O número de iterações necessárias foram {iteracao}.")