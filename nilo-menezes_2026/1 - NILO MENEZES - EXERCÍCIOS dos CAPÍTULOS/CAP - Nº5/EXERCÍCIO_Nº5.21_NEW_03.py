# ENUNCIADO — O Contador de Pacotes
#
# Uma transportadora envia decompor em pacotes de:
#   12 kg
#   5 kg
#   1 kg
#
# Escreva um programa que:
#
# 1. Peça ao utilizador um peso total (inteiro positivo).
# 2. O programa deve decompor esse peso usando pacotes de 12 kg, depois 5 kg, depois 1 kg.
# 3. O programa deve mostrar quantos pacotes de cada tipo foram usados.
# 4. O programa deve repetir enquanto o utilizador não digitar 0.
# 5. Ao digitar 0, o programa termina.
#
# Regras:
# - Comece sempre pelo total_pacotes de 12 kg.
# - Quando já não conseguir tirar mais pacotes desse tipo, passe para o total_pacotes seguinte.
# - Use while True e condições aninhadas.
# - Não use listas, funções ou nada fora do Capítulo 5.


while True:
    # Peço o peso total ao utilizador.
    total = int(input('Digite um total (valor inteiro) para enviar! Para terminar digite "0": '))

    # Se for 0, termino o programa.
    if total == 0:
        break

    # Aqui começo a decompor o valor.
    decompor = total  # Eu tinha usado "total" dentro do loop interno, o que era errado.
                      # O correto é usar "decompor", para não destruir o valor original.
    pacotes = 12      # Começo sempre pelo pacote maior.
    total_pacotes = 0 # Contador de pacotes do tipo atual.

    while True:
        # ERRO ORIGINAL:
        # Eu escrevi "if total >= 12", mas isso está errado.
        # Porque "total" já foi sendo alterado, e eu devia usar "decompor".
        if pacotes <= decompor: # PODIA TAMBÉM TER COLOCADO: "decompor >= pacotes: QUE CONTINUAVA CORRETO 
            # Subtraio o pacote ao valor que falta decompor.
            decompor -= pacotes
            total_pacotes += 1
        else:
            # Quando já não consigo tirar mais pacotes deste tipo, mostro o total.
            print(f"Foram usados {total_pacotes} pacote(s) de {pacotes} kg")

            # ERRO ORIGINAL:
            # Eu verificava "if decompor == 0" mas tinha usado "total" no loop.
            # Agora sim, faz sentido.
            if decompor == 0:
                break

            # Agora mudo para o próximo pacote.
            # ERRO ORIGINAL:
            # Eu tinha escrito:
            # if pacotes == 12: pacotes = 5
            # if pacotes == 5: pacotes = 1
            # Isto funciona, mas é frágil.
            if pacotes == 12:
                pacotes = 5
            elif pacotes == 5:
                pacotes = 1

            # Reinicio o contador para o novo tipo de pacote.
            total_pacotes = 0



        





