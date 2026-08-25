# ENUNCIADO

# Escreva um programa que leia repetidamente idades de pessoas.
# O programa deve parar apenas quando o utilizador digitar 999.

# - A idade deve ser validada:
# - Só são aceites idades entre 0 e 120 anos.
# - Enquanto a idade estiver fora deste intervalo, o programa deve pedir um novo valor.

#   Depois de validada, a idade deve ser classificada assim:

# 0 a 12   → "Criança"
# 13 a 17  → "Adolescente"
# 18 a 64  → "Adulto"
# 65 a 120 → "Idoso"

# O programa deve mostrar:

# - idades total de idades introduzidas
# - idades de "Criança"
# - idades de "Idoso"
# - Soma total das idades (para calcular a média)
# - A idade mais alta registada
# - A idade mais baixa registada

# No final (quando o utilizador digitar 999), o programa deve mostrar:

# - Total de idades introduzidas                
# - Média das idades (com 2 casas decimais)
# - Idade mais alta
# - Idade mais baixa
# - Quantas foram "Criança"
# - Quantas foram "Idoso"
# - Percentagem de "Criança"
# - Percentagem de "Idoso"

########################################################################################
#                                   = RESOLUÇÃO =                                      #
# ######################################################################################
# ---------------------------------------------------------
# Inicialização das variáveis
# ---------------------------------------------------------

idades_total = 0            # Conta quantas idades válidas foram introduzidas
idades_criancas = 0         # Conta quantas pessoas são crianças
idades_idosos = 0           # Conta quantas pessoas são idosas

idade_mais_baixa = 120      # Começa no máximo possível para depois ir descendo
idade_mais_alta = 0         # Começa no mínimo possível para depois ir subindo

soma_total_idades = 0       # Acumulador para calcular a média das idades



while True:
    print("\nEste programa vai pedir um conjunto de idades e classificá-las.")
    idade = float(input("Digite a idade pretendida (999 para parar): "))

    if idade == 999:
        print("O programa para.")
        break

    if idade < 0 or idade > 120:
        print("Idade fora dos parâmetros. Digite novamente!")
        continue   # Volta ao início do ciclo sem contar esta idade que estava errada!

    idades_total += 1            # Incrementa o número total de pessoas
    soma_total_idades += idade   # Soma para calcular a média

    if idade > idade_mais_alta:
        idade_mais_alta = idade

    if idade < idade_mais_baixa:
        idade_mais_baixa = idade

    if idade <= 12:
        print("Criança")
        idades_criancas += 1

    elif idade <= 17:
        print("Adolescente")

    elif idade <= 64:
        print("Adulto")

    else:
        print("Idoso")
        idades_idosos += 1


# ---------------------------------------------------------
# Análises finais (apenas se houver idades válidas)
# ---------------------------------------------------------

if idades_total > 0:
    print("\nAnálises obtidas:")
    print(f"O total de pessoas é: {idades_total}")
    print(f"A média das idades é: {soma_total_idades / idades_total:.2f}")
    print(f"A idade mais alta é: {idade_mais_alta} anos")
    print(f"A idade mais baixa é: {idade_mais_baixa} anos")
    print(f"O número de crianças é: {idades_criancas}")
    print(f"O número de idosos é: {idades_idosos}")

    # Percentagens corretas: dividem pelo total de pessoas
    print(f"A percentagem de crianças é: {(idades_criancas / idades_total) * 100:.2f}%")
    print(f"A percentagem de idosos é: {(idades_idosos / idades_total) * 100:.2f}%")

else:
    print("\nNão foram introduzidas idades válidas.")

