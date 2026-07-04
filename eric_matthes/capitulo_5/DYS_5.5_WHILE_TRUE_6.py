# ENUNCIADO

# Escreva um programa que leia repetidamente notas de alunos entre 0 e 20.
# O programa deve parar apenas quando o utilizador digitar 999.

# A nota deve ser validada:
# - Só são aceites valores entre 0 e 20.
# - Enquanto a nota estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validada, a nota deve ser classificada assim:

# 0 a 4   → "Mau"
# 5 a 9   → "Insuficiente"
# 10 a 13 → "Suficiente"
# 14 a 17 → "Bom"
# 18 a 20 → "Excelente"

# O programa deve manter:

# - Contador total de notas introduzidas                
# - Contador de notas "Excelente"                       
# - Contador de notas "Mau"                             
# - Soma total das notas (para calcular a média)        
# - A nota mais alta registada
# - A nota mais baixa registada

# No final (quando o utilizador digitar 999), o programa deve mostrar:

# - Total de notas introduzidas
# - Média das notas (com 2 casas decimais)
# - Nota mais alta
# - Nota mais baixa
# - Quantas foram "Excelente"
# - Quantas foram "Mau"
# - Percentagem de "Excelente"
# - Percentagem de "Mau"

# Não usar listas, nem funções, nem try/except.
# Usar apenas:
# - while True
# - while de validação
# - if/elif/else
# - contadores
# - acumuladores
# - break


########################################################################################
#                                   = RESOLUÇÃO =                                      #
# ######################################################################################
    
total_notas = 0
notas_mau = 0
notas_excelente = 0

soma_notas = 0
nota_mais_alta = 0
nota_mais_baixa = 20        # SUPER IMPORTANTE: começa no máximo possível a nota mais baixa.

while True:
    print("Este programa vai registar as notas dos alunos, e analisá-las! Os valores variam entre '0' e '20'")

    notas = int(input("Introduza todas as notas dos alunos: "))

    # SENTINELA
    if notas == 999:
        print("Programa terminado pelo utilizador.")
        break

    # VALIDAÇÃO
    while notas < 0 or notas > 20:
        print("Nota inválida!")
        notas = int(input("A nota que inseriu não está no intervalo definido. Corrija! "))

    # CONTADOR PRINCIPAL (só conta notas válidas)
    total_notas += 1            # SUPER IMPORTANTE: O contador dentro da validação NÃO conta notas válidas (SE ESTIVESSE INDENTADO AO "WHILE"). 
                                # O contador dentro da validação contava APENAS valores inválidos!
    # SOMA DAS NOTAS (para média)
    soma_notas += notas

    # NOTA MAIS ALTA
    if notas > nota_mais_alta:
        nota_mais_alta = notas

    # NOTA MAIS BAIXA
    if notas < nota_mais_baixa:
        nota_mais_baixa = notas

    # CLASSIFICAÇÃO
    if notas <= 4:
        print("Mau")
        notas_mau += 1

    elif notas <= 9:
        print("Insuficiente")

    elif notas <= 13:
        print("Suficiente")

    elif notas <= 17:
        print("Bom")
    
    else:
        print("Excelente")
        notas_excelente += 1

# RESULTADOS FINAIS
print("\nApresentação dos Resultados")
print(f"Foram introduzidas {total_notas} notas no programa.")
print(f"A média das notas foi de: {soma_notas / total_notas:5.2f}")
print(f"A nota mais alta foi: {nota_mais_alta} valores")
print(f"A nota mais baixa foi: {nota_mais_baixa} valores")
print(f"Percentagem de notas 'Excelente': {(notas_excelente / total_notas) * 100:5.2f}%")
print(f"Percentagem de notas 'Mau': {(notas_mau / total_notas) * 100:5.2f}%")
