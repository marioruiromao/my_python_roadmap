# EXERCÍCIO — CAPÍTULO 5 (Ciclos + Validação)
#
# Escreva um programa que peça ao utilizador a sua idade.
#
# O programa deve validar a entrada:
#   - A idade deve estar entre 0 e 120.
#   - Se o utilizador escrever um valor inválido, deve mostrar uma mensagem de erro
#     e pedir novamente.
#
# Depois de validar a idade, o programa deve:
#   - Mostrar uma mensagem adequada:
#       - Menor de idade (0 a 17)
#       - Adulto (18 a 64)
#       - Sénior (65 a 120)
#
# O programa deve continuar a pedir idades até o utilizador escrever 99.
#
# Quando o utilizador escrever 99, o programa termina e mostra:
#   - "Programa encerrado."
#
# Regras:
#   - Usa apenas while, if/elif/else, variáveis simples e validação.
#   - Não uses listas.
#   - Usa break para parar quando o utilizador digitar 99.

while True:
    idade = int(input("Diga, por favor, a sua idade! Para parar digite '99': "))

    # Se o utilizador digitar 99, o programa deve parar imediatamente.
    if idade == 99:
        print("O programa vai encerrar!")
        break  # Uso o break porque estou dentro de um ciclo while.

    # Validação contínua: SUPER IMPORTNATE: Enquanto a idade for inválida (menor que 0 ou maior que 120),
    # o programa continua a pedir até o utilizador escrever um valor correto.
    while idade < 0 or idade > 120:
        print("Introduziu um valor errado!")
        idade = int(input("Diga, por favor, a sua idade novamente!: "))

    # A partir daqui, a idade é garantidamente válida (0 a 120).
    # Agora classifico a idade por faixas etárias.

    if idade <= 17:
        # Se a idade estiver entre 0 e 17, é menor de idade.
        print("Menor de idade.")

    elif idade <= 64:
        # Se a idade estiver entre 18 e 64, é adulto.
        print("É adulto!")

    elif idade

        
# SUPER DICA: NUNCA ESQUECER: “Se algo pode estar errado, eu tenho de repetir até estar certo.”

