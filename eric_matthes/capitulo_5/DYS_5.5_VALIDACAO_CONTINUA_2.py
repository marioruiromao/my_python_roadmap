# EXERCÍCIO — CAPÍTULO 5 (Ciclos + Validação)
#
# Escreva um programa que peça ao utilizador a temperatura atual em graus Celsius.
#
# O programa deve validar a entrada:
#   - A temperatura deve estar entre -50 e 50 graus.
#   - Se o utilizador escrever um valor fora deste intervalo,
#     deve mostrar uma mensagem de erro e pedir novamente.
#
# Depois de validar a temperatura, o programa deve:
#   - Mostrar uma mensagem adequada:
#       - "Está muito frio!"  (temperatura <= 5)
#       - "Temperatura agradável." (6 a 25)
#       - "Está muito calor!" (26 a 50)
#
# O programa deve continuar a pedir temperaturas até o utilizador escrever 99.
#
# Quando o utilizador escrever 99, o programa termina e mostra:
#   - "Programa encerrado."
#
# Regras:
#   - Usa apenas while, if/elif/else, variáveis simples e validação.
#   - Não uses listas.
#   - Usa break para parar quando o utilizador digitar 99.


while True:
    print("Diga uma temperatura no intervalo de -50 a 50 graus. Vamos classificá-la!")
    temperatura = float(input("Digite a temperatura em graus Celsius. Para parar escreva '99':"))

    if temperatura == 99:
        print("Programa encerrado!")
        break
    # A REGRA DE OURO (que resolve tudo): Validação repete. Classificação não repete. Por isso, VALIDAÇÃO fica dentro do while. CLASSIFICAÇÃO fica fora.
    # Validação = while
    # Classificação = if / elif / else
    while temperatura < -50 or temperatura > 50: # Este while é um filtro. Não é uma classificação, serve apenas para validação.
        print("Erro! Temperatura fora dos parâmetros!")
        temperatura = float(input("Digite uma nova temperatura dentro do intervalo definido: "))
        
    if temperatura <= 5:    # NBH - Se os "if/elif" estivessem indentados dentro do "while", o programa nunca mais parava.
        print("Está muito frio!")
    elif temperatura <= 25:
        print("Temperatura agradável!")
    else:
        print("Está muito calor :((")




# COMO DEVO ETRUTURAR O MEU PENSAMENTO:

#       while True:
#           ler temperatura
#           se for 99 → break
#           e for inválida → pedir outra
#           senão → classificar
#
#       Validação = while (repete até estar certo).
#
#       Classificação = if/elif/else (executa uma vez).