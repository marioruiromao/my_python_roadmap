# ENUNCIADO

# Escreva um programa que leia repetidamente temperaturas.
# O programa deve parar apenas quando o utilizador digitar 000.

# A temperatura deve ser validada: só são aceites valores entre -30 e 50 graus.
# Enquanto a temperatura estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validada, a temperatura deve ser classificada da seguinte forma:

# -30 a 0      → "Frio Extremo"
# 1 a 15       → "Frio"
# 16 a 25      → "Agradável"
# 26 a 35      → "Quente"
# 36 a 50      → "Calor Extremo"

# O programa deve também calcular:
#       - O número total de temperaturas válidas
#       - A soma total das temperaturas
#       - A temperatura mais alta registada
#       - A temperatura mais baixa registada
#       - O número de temperaturas "Frio Extremo"
#       - O número de temperaturas "Calor Extremo"
#       - A percentagem de "Frio Extremo" e "Calor Extremo" em relação ao total

# No final, o programa deve apresentar todas estas análises.

# Regras obrigatórias:
# - Usar apenas: while True, validação com if, continue, break, if/elif/else, contadores e acumuladores.
# - Não usar listas, funções, módulos ou estruturas avançadas.
########################################################################################
#                                   = RESOLUÇÃO =                                      #
# ######################################################################################

# Aqui estou a iniciar os contadores e acumuladores
total_temperaturas = 0
temperatura_mais_alta = -30
temperatura_mais_baixa = 50
frio_extremo = 0
calor_extremo = 0
soma_total_temperaturas = 0

while True:
    temperatura = float(input("Digite uma temperatura em ºC (777 para parar): "))

    if temperatura == 777:
        print("Programa encerrado!")
        break

    if temperatura < -30 or temperatura > 50:
        print("Erro! Valor inválido. Digite novamente!")
        continue  # Aqui estou a impedir que valores inválidos sejam contados

   # O meu erro foi usar >=, que não faz sentido para máximos
    if temperatura > temperatura_mais_alta:
        temperatura_mais_alta = temperatura

    if temperatura < temperatura_mais_baixa:
        temperatura_mais_baixa = temperatura

    # Aqui estou a contar temperaturas válidas
    total_temperaturas += 1

    # Vou classificar as temperaturas
    if temperatura <= 0:
        print("Frio extremo")
        frio_extremo += 1
    elif temperatura <= 15:
        print("Frio")
    elif temperatura <= 25:
        print("Agradável")
    elif temperatura <= 35:
        print("Quente")
    else:
        print("Calor extremo")
        calor_extremo += 1

    # Aqui estou a somar todas as temperaturas
    soma_total_temperaturas += temperatura

# Muito importante: aqui vou garantir que não divido por zero!
if total_temperaturas > 0:
    print("\nApresentação dos resultados:")
    print("O número de temperaturas válidas é:", total_temperaturas)
    print(f"A soma total das temperaturas é: {soma_total_temperaturas}")
    print(f"A temperatura mais alta foi: {temperatura_mais_alta} ºC")
    print(f"A temperatura mais baixa foi: {temperatura_mais_baixa} ºC")
    print("Ocorrências de 'Frio Extremo':", frio_extremo)
    print("Ocorrências de 'Calor Extremo':", calor_extremo)

    # Erro corrigido: percentagens dividem pelo total de elementos
    print(f"Percentagem de 'Calor Extremo': {(calor_extremo / total_temperaturas) * 100:.2f}%")
    print(f"Percentagem de 'Frio Extremo': {(frio_extremo / total_temperaturas) * 100:.2f}%")
else:
    print("Nenhuma temperatura válida foi introduzida.")

# NOTA IMPORTANTE: Como evitar isto para sempre (regra do mestre)
# Sempre que fores calcular:
#       - Média
#       - Percentagem
#       - Proporção
#       - Razão


   
    

    




