# ENUNCIADO — O Distribuidor de Caixas
#
# Uma fábrica embala produtos em caixas de:
#   20 unidades
#   8 unidades
#   2 unidades
#
# Escreva um programa que:
#
# 1. Peça ao utilizador um número total de produtos (inteiro positivo).
# 2. O programa deve decompor esse total usando caixas de 20, depois 8, depois 2 unidades.
# 3. O programa deve mostrar quantas caixas de cada tipo foram usadas.
# 4. O programa deve repetir enquanto o utilizador não digitar 0.
# 5. Ao digitar 0, o programa termina.
#
# Regras:
# - Comece sempre pela caixa de 20 unidades.
# - Quando já não conseguir tirar mais caixas desse tipo,
#   passe para a caixa seguinte.
# - Use while True e condições aninhadas.
# - Não use listas, funções ou nada fora do Capítulo 5.

while True:
    produtos = int(input('Digite o seu número (inteiro) de produtos. Para parar, digite "0"! '))
    if produtos == 0:
        break

    # ERRO ORIGINAL:
    # Eu tinha colocado "decompor = 0", o que destrói o valor inicial.
    # O correto é copiar o valor para uma variável que vou subtrair.
    decompor = produtos  # Agora sim: decompor começa igual ao total.
    caixas = 20          # Começo sempre pela caixa maior.
    total_caixas = 0     # Contador de caixas do tipo atual.

    while True:         # ERRO ORIGINAL: Eu escrevi "if produtos >= caixas", mas "produtos" nunca muda.
                        # A variável que muda é "decompor".
        if decompor >= caixas:
            # Subtraio o tamanho da caixa ao que falta.
            decompor -= caixas
            total_caixas += 1
        else:
            # ERRO ORIGINAL:
            # A frase estava trocada: "Foram usadas 20 caixas num total de X produtos"
            # O correto é mostrar quantas caixas foram usadas.
            print(f"Foram usadas {total_caixas} caixa(s) de {caixas} unidades")

            # Se já não falta nada, termino o loop interno.
            if decompor == 0:
                break
        
            if caixas == 20:        #COMO LER: Se caixas for igual a vinte…
                caixas = 8          #           …então caixas passa a valer oito
            elif caixas == 8:       #           Caso contrário, se caixas for igual a oito…
                caixas = 2          #           …então caixas passa a valer dois.
            elif caixas == 2:       #           Caso contrário, se caixas for igual a dois…
                break               #           …então termina o ciclo.
                        
            total_caixas = 0        # Tenho que ter esta condição, porque a cada ciclo (20, 8 e 2) começo do REÍNICIO! 
