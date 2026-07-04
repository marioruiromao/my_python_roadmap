# ENUNCIADO:

# Escreva um programa que leia repetidamente valores de consumo de energia elétrica
# (em kWh — quilowatt-hora).

# O programa deve parar apenas quando o utilizador digitar 999.

# O consumo deve ser validado: só são aceites valores entre 0 e 2000 kWh.
# Enquanto o consumo estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validado, o consumo deve ser classificado da seguinte forma:

# 0 a 100 kWh        → "Consumo muito baixo"
# 101 a 300 kWh      → "Consumo baixo"
# 301 a 600 kWh      → "Consumo moderado"
# 601 a 1200 kWh     → "Consumo alto"
# 1201 a 2000 kWh    → "Consumo muito alto"

# O programa deve também calcular:
# - O número total de consumos válidos  -S
# - A soma total dos consumos   -S
# - O consumo mais alto registado   -S
# - O consumo mais baixo registado  -S
# - O número de consumos "muito baixo"   -S
# - O número de consumos "muito alto"    -S
# - A percentagem de "muito baixo" e "muito alto" em relação ao total

# No final, o programa deve apresentar todas estas análises.

# Regras obrigatórias:
# - Usar apenas: while True, validação com if, continue, break, if/elif/else,
#   contadores e acumuladores.
# - Não usar listas, funções, módulos ou estruturas avançadas.
# - Mostrar os resultados APENAS no final do programa.

###############################################################################
#                               RESOLUTION                                    #
###############################################################################

"""
Programa de leitura e análise de consumos eléctricos.
Valores válidos: 0 a 2000 Kwh.
O utilizador termina com 999.
"""

total_consumos = 0
soma_total_consumos = 0
consumo_muito_baixo = 0
consumo_muito_alto = 0

consumo_mais_alto = 0
consumo_mais_baixo = 2000

while True:
    consumo = float(input("Insira o consumo (Kwh). Para parar, digite 999: "))

    if consumo == 999:
        print("\nPrograma encerrado!")
        break

    if not 0 <= consumo <= 2000:
        print("Erro! Valor inválido.")
        continue

    total_consumos += 1
    soma_total_consumos += consumo

    consumo_mais_alto = max(consumo_mais_alto, consumo)
    consumo_mais_baixo = min(consumo_mais_baixo, consumo)

    if consumo <= 100:
        print("Consumo muito baixo")
        consumo_muito_baixo += 1
    elif consumo <= 300:
        print("Consumo baixo")
    elif consumo <= 600:
        print("Consumo moderado")
    elif consumo <= 1200:
        print("Consumo alto")
    else:
        print("Consumo muito alto")
        consumo_muito_alto += 1

if total_consumos == 0:
    print("Nenhum consumo válido foi registado.")
else:
    print("\n--- Resultados Finais ---")
    print(f"Total de consumos: {total_consumos}")
    print(f"Consumo total: {soma_total_consumos:.2f} Kwh")
    print(f"Consumo mais alto: {consumo_mais_alto}")
    print(f"Consumo mais baixo: {consumo_mais_baixo}")
    print(f"Consumos muito baixos: {consumo_muito_baixo}")
    print(f"Consumos muito altos: {consumo_muito_alto}")
    print(f"Percentagem muito baixos: {(consumo_muito_baixo / total_consumos) * 100:.2f}%")
    print(f"Percentagem muito altos: {(consumo_muito_alto / total_consumos) * 100:.2f}%")




     

    


