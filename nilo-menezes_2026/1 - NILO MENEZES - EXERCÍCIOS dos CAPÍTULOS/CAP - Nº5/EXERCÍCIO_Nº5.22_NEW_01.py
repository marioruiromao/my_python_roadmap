
# ------------------------------------------------------------
# EXERCÍCIO — TABUADA COM INTERVALO PERSONALIZADO (SEM DICIONÁRIOS)
# ------------------------------------------------------------
#
# Crie um programa que apresente o seguinte menu:
#
# 1 - Adição
# 2 - Subtração
# 3 - Divisão
# 4 - Multiplicação
# 5 - Exit
#
# O programa deve funcionar assim:
#
# 1. O utilizador escolhe uma opção do menu.
#
# 2. Se escolher a opção 5, o programa deve terminar imediatamente.
#
# 3. Se escolher uma operação válida (1 a 4):
#       - O programa deve pedir um número base para gerar a tabuada.
#       - Depois deve pedir:
#             * Um número inicial para começar a tabuada
#             * Um número final para terminar a tabuada
#
# 4. O programa deve então mostrar a tabuada da operação escolhida,
#    desde o número inicial até ao número final.
#
# 5. O programa deve repetir o menu até o utilizador escolher a opção 5.
#
# Regras:
# - Não utilizar dicionários.
# - Utilizar apenas while, if/elif/else, variáveis e f-strings.
# - O programa deve ser simples e seguir a estrutura que já aprendeste.
#


#               ------------ RESOLUÇÃO -----------
while True:
    print("""
           1 - Adição 
           2 - Subtração 
           3 - Divisão 
           4 - Multiplicação 
           5 - Exit
    """)

    tabuada = int(input('Qual é a operação que deseja? Escolha o número da tabuada! Para sair prima "5". '))

    if tabuada == 5:
        break

    elif 1 <= tabuada < 5:

        primeiro_numero = int(input('Qual é o primeiro número da tabuada: '))
        ultimo_numero = int(input('Diga qual é o último número da tabuada: '))

        x = primeiro_numero

        while x <= ultimo_numero:

            if tabuada == 1:
                print(f'{x} + {primeiro_numero} = {x + primeiro_numero}')

            elif tabuada == 2:
                print(f'{x} - {primeiro_numero} = {x - primeiro_numero}')

            elif tabuada == 3:
                print(f'{x} / {primeiro_numero} = {x / primeiro_numero:^10.2f}')

            elif tabuada == 4:
                print(f'{x} x {primeiro_numero} = {x * primeiro_numero}')

            x += 1

    else:
        print('Erro!')

# SUPER IMPORTANTE:
# # ------------------------------------------------------------
# POSSO USAR while True NO 2º WHILE?
# ------------------------------------------------------------
#
# RESPOSTA CURTA: Não. No teu caso específico, usar while True no 2º loop seria errado.
#
# FUNDAMENTAÇÃO:
#
# 1) O 2º while controla a tabuada entre dois limites:
#       while inicio <= fim
#    Isto é um loop com limite conhecido.
#
# 2) Quando o número de repetições é conhecido,
#    a boa prática é usar uma condição explícita.
#
# 3) IMPORTANTE: Se usasses while True aqui, o loop nunca terminaria,
#    porque dentro dele não existe nenhum break.
#
# 4) Resultado: o programa ficaria preso num loop infinito.
#
# 5) while True só deve ser usado quando:
#                - o número de repetições é desconhecido
#                - existe um break claro dentro do loop
#    Exemplo típico: menus.
#
# CONCLUSÃO:
# O 2º while deve continuar com:
#       while inicio <= fim
# porque é um loop controlado por contagem.
# ------------------------------------------------------------
