# ENUNCIADO — O Embalador de Sacos de Arroz
#
# Uma empresa embala arroz em sacos de:
#   15 kg
#   6 kg
#   3 kg
#
# Escreva um programa que:
#
# 1. Peça ao utilizador um peso total (inteiro positivo) de arroz.
# 2. O programa deve decompor esse peso usando sacos de 15 kg, depois 6 kg, depois 3 kg.
# 3. O programa deve mostrar quantos sacos de cada tipo foram usados.
# 4. O programa deve repetir enquanto o utilizador não digitar 0.
# 5. Ao digitar 0, o programa termina.
#
# Regras:
# - Comece sempre pelo saco de 15 kg.
# - Quando já não conseguir tirar mais sacos desse tipo,
#   passe para o saco seguinte.
# - Use while True e condições aninhadas.
# - Não use listas, funções ou nada fora do Capítulo 5.

while True:
    peso_total_arroz = int(input("Digite o peso total (valor positivo) de arroz. Para parar digite '0'! "))
    
    if peso_total_arroz == 0:
        break

    decompor = peso_total_arroz     # SUPER IMPORTANTE: A ORDEM É EXTREMAMENTE IMPORTANTES!!! 
    sacos_arroz = 15                # A ordem correta é: 1 - Definir o tipo de saco inicial; 2 - Copiar o valor para decompor; 3 - Inicializar o contador
    sacos = 0

    while True:
        if decompor >= sacos_arroz:
            decompor -= sacos_arroz
            sacos += 1
        else:
            print(f"Foram usados {sacos} sacos de {sacos_arroz}Kg ")

            if decompor == 0:
                break

            # ESTA PARTE TEM DE ESTAR DENTRO DO ELSE
            if sacos_arroz == 15:
                sacos_arroz = 6
            elif sacos_arroz == 6:
                sacos_arroz = 3
            elif sacos_arroz == 3:
                break
            
            sacos = 0
