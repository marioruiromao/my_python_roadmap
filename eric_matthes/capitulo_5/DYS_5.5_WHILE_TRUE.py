# EXERCÍCIO — CAPÍTULO 5 (Ciclos + Validação)
# 
# Escreva um programa que peça ao utilizador uma nota entre 0 e 10.
# 
# O programa deve validar a entrada:
#   - Se o utilizador escrever um valor fora do intervalo (menor que 0 ou maior que 10),
#     deve mostrar uma mensagem de erro e pedir novamente.
#
# Quando o utilizador finalmente escrever uma nota válida,
# o programa deve mostrar:
#   - "Nota registada com sucesso!"
#
# Depois disso, o programa deve:
#   - Continuar a pedir notas até o utilizador escrever o número 99.
#
# Quando o utilizador escrever 99, o programa termina e mostra:
#   - "Programa encerrado."
#
# Regras:
#   - Usa apenas while, if/elif/else, variáveis simples e validação.
#   - Não uses listas avançadas (apenas o básico do CAP 5).



while True:
    nota = int(input("Escreva uma nota entre '0' e '10'. Para parar digite 99! "))

    if nota == 99:
        print("Programa encerrado.")
        break   # pára o ciclo e termina o programa

    if nota < 0 or nota > 10:
        print("Valor inválido! A nota deve estar entre 0 e 10.")
    else:
        print("Nota registada com sucesso!")

