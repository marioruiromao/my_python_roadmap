# ENUNCIADO:

# Escreva um programa que leia repetidamente notas de alunos entre 0 e 20.
# O programa deve parar apenas quando o utilizador digitar 999.

# A nota deve ser validada: só são aceites valores entre 0 e 20.
# Enquanto a nota estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validada, a nota deve ser classificada assim:

# 0 a 4   → "Mau"
# 5 a 9   → "Insuficiente"
# 10 a 13 → "Suficiente"
# 14 a 17 → "Bom"
# 18 a 20 → "Excelente"

# O programa deve também manter contadores:
# - Quantas notas foram introduzidas
# - Quantas notas foram "Excelente"
# - Quantas notas foram "Mau"

# No final (quando o utilizador digitar 999), o programa deve mostrar:

# - Total de notas introduzidas
# - Quantas foram "Excelente"
# - Quantas foram "Mau"

# Não usar listas, nem funções, nem estruturas avançadas.
# Usar apenas: while True, while de validação, if/elif/else, contadores e break.

# #######################################################################################
#                                   = RESOLUÇÃO =
# #######################################################################################

# SUPER NOTA: Criação dos contadores = FORA do while True
# SUPER NOTA: Todos os incrementos = DENTRO do while True.

# CONTADORES — criados antes do while True
total_notas = 0
excelentes = 0
maus = 0

while True:
    print("Programa: classificação das notas de alunos! Valores: entre '0' e '20'. Para parar, digite '999'")

    notas = int(input("Classificação do aluno. Introduza a nota do aluno - de '0' a '20': "))

    # SENTINELA — parar o programa
    if notas == 999:
        print("Parar! O programa foi interrompido!")
        break

    # VALIDAÇÃO — repetir até estar certo. Só são aceites valores dentro deste intervalo, caso contrário continua a REPETIR.
    while notas < 0 or notas > 20: 
        print("Erro! Nota inválida! Introduza novamente.")
        notas = int(input("Volte a introduzir uma nota de '0' a '20': "))

    # CONTADOR PRINCIPAL — só conta notas válidas (total_notas). Incrementa uma vez por nota válida, LOGO APÓS a VALIDAÇÃO.
    total_notas += 1

    # CLASSIFICAÇÃO + CONTADORES ESPECÍFICOS
    if notas <= 4:
        print("Nota final: 'Mau'")
        maus += 1
    elif notas <= 9:
        print("Nota final: 'Insuficiente'")
    elif notas <= 13:
        print("Nota final: 'Suficiente'")
    elif notas <= 17:
        print("Nota final: 'Bom'")
    else:
        print("Obteve a nota 'Excelente'. Parabéns!")
        excelentes += 1

# RESULTADOS FINAIS
print("\n--- ESTATÍSTICAS FINAIS ---")
print(f"Total de notas introduzidas: {total_notas}")
print(f"Notas 'Excelente': {excelentes}")
print(f"Notas 'Mau': {maus}")



