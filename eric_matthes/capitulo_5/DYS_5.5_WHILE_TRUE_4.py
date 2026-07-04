# ENUNCIADO

# Escreva um programa que leia repetidamente uma velocidade em km/h.
# O programa deve parar apenas quando o utilizador digitar 999.

# A velocidade deve ser validada: só são aceites valores entre 0 e 200 km/h.
# Enquanto a velocidade estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validada, a velocidade deve ser classificada da seguinte forma:

# 0 a 20      → "Muito lento"
# 21 a 80     → "Velocidade normal"
# 81 a 120    → "Rápido"
# 121 a 200   → "Muito rápido!"

# Não usar listas, nem funções, nem estruturas avançadas.
# Usar apenas: while True, while de validação, if/elif/else e break.

while True: # O ciclo principal controla o programa
    print("Vamos classificar a sua velocidade. Os valores aceites variam entre 0 e 200km/h")

    velocidade = int(input("Diga a velocidade em km/h. Para parar, digite '999': "))

    if velocidade == 999:
        print("Ordem para parar!")
        break

    # Validação correta: aqui SÓ avançamos com valores corretos, caso contrário continua a perguntar! NÃO DEIXA AVANÇAR! 
    while velocidade < 0 or velocidade > 200:   # Validação = while (repete até estar certo)
        print("Só são aceites valores entre 0km/h e 200km/h")
        velocidade = int(input("Digite uma velocidade dentro deste intervalo de velocidades: "))

    # Classificação
    if velocidade <= 20:
        print('Muito lento')
    elif velocidade <= 80:
        print('Velocidade normal')
    elif velocidade <= 120:
        print('Rápido')
    else:
        print('Muito rápido') # Podia usal um "elif", garante um resultado mais seguro!

