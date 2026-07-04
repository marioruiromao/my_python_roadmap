# ENUNCIADO

# Escreva um programa que leia repetidamente temperaturas em graus Celsius.
# O programa deve parar apenas quando o utilizador digitar 999.

# A temperatura deve ser validada: só são aceites temperaturas entre -30 e 50.
# Enquanto a temperatura estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validada, a temperatura deve ser classificada assim:

# -30 a 0   → "Muito frio"
# 1 a 15    → "Frio"
# 16 a 25   → "Agradável"
# 26 a 35   → "Quente"
# 36 a 50   → "Muito quente"

# O programa deve também manter contadores:
# - Quantas temperaturas foram introduzidas
# - Quantas foram "Muito frio"
# - Quantas foram "Muito quente"

# No final (quando o utilizador digitar 999), o programa deve mostrar:

# - Total de temperaturas introduzidas
# - Quantas foram "Muito frio"
# - Quantas foram "Muito quente"

# Não usar listas, nem funções, nem estruturas avançadas.
# Usar apenas: while True, while de validação, if/elif/else, contadores e break.

# #######################################################################################
#                                   = RESOLUÇÃO =
# #######################################################################################

                                        # SUPER NOTA: Criação dos CONTADORES = FORA do while True

                                        # SUPER NOTA: Todos os INCREMENTOS = DENTRO do while True.

total_temperaturas = 0
muito_frio = 0
muito_quente = 0

while True:
    print("Vamos classificar as suas temperaturas. Para interromper, digite: '999' ")

    temperatura = int(input("Introduza as temperaturas em graus Celsius: "))

    if temperatura == 999: # SENTINELA
        print("Contagem interrompida!")
        break

    while temperatura < -30 or temperatura > 50:
        print("Erro! Temperaturas fora dos parâmetros!")
        temperatura = int(input("Os valores da temperatura têm de estar dentro do intervalo definido! "))
    
    total_temperaturas += 1
    
    if temperatura <= 0:
        print("Muito frio!")
        muito_frio += 1

    elif temperatura <= 15:
        print("Frio!")

    elif temperatura <= 25:
        print("Agradável!")

    elif temperatura <= 35:
        print("Quente!")
        
    else:
        print("Muito quente!")
        muito_quente += 1
    
print("\nEstatísticas finais das temperaturas registadas: ")
print(f"O total das temperaturas introduzidas foram: {total_temperaturas} temperaturas. ")
print(f"Foram introduzidas {muito_frio} temperaturas consideradas muito frias. ")
print(f"Foram introduzidas {muito_quente} temperaturas consideradas muito quentes. ")



