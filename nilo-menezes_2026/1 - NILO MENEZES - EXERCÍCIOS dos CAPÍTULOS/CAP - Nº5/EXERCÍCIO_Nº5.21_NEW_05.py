# ENUNCIADO — O Distribuidor de Garrafas
#
# Uma fábrica distribui bebidas em garrafas de:
#   9 litros
#   4 litros
#   1 litro
#
# Escreva um programa que:
#
# 1. Peça ao utilizador um volume_garrafas total (inteiro positivo) em litros.
# 2. O programa deve decompor esse volume_garrafas usando garrafas de 9 L, depois 4 L, depois 1 L.
# 3. O programa deve mostrar quantas garrafas de cada tipo foram usadas.
# 4. O programa deve repetir enquanto o utilizador não digitar 0.
# 5. Ao digitar 0, o programa termina.
#
# Regras:
# - Comece sempre pela garrafa de 9 litros.
# - Quando já não conseguir tirar mais garrafas desse tipo,
#   passe para a garrafa seguinte.
# - Use while True e condições aninhadas.
# - Não use listas, funções ou nada fora do Capítulo 5.

while True:
    volume_garrafas = int(input("Diga quantos litros vais usar (um número inteiro)? Para parar digite '0': "))

    if volume_garrafas == 0:
        break

    decompor = volume_garrafas
    garrafas = 9
    tipos_garrafa = 0

    while True:
        if decompor >= garrafas:
            decompor -= garrafas
            tipos_garrafa += 1
        else:
            print(f"Foram usadas {tipos_garrafa} garrafa(s) de {garrafas} litros")

            if decompor == 0:
                break

            if garrafas == 9:
                garrafas = 4
            elif garrafas == 4:
                garrafas = 1
            elif garrafas == 1:
                break

            tipos_garrafa = 0




