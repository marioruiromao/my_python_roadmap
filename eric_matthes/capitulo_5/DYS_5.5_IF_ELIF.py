# EXERCÍCIO — CAPÍTULO 5 (NILO MENEZES)
#
# Cria um programa que simule um pequeno jogo de pontuação baseado em cores.
#
# 1. Cria uma lista simples com três cores:
#    - 'green'
#    - 'yellow'
#    - 'red'
#
# 2. Mostra a lista ao utilizador.
#
# 3. Pede ao utilizador que escolha uma cor.
#    - Garante que removes espaços antes/depois (strip)
#    - Garante que transformas tudo em minúsculas (lower)
#
# 4. Primeiro: valida se a cor escolhida existe na lista.
#    - Se NÃO existir, mostra uma mensagem de erro.
#
# 5. Se existir, mostra a pontuação correspondente:
#    - green  → 10 pontos
#    - yellow → 500 pontos
#    - red    → 8000 pontos
#
# 6. Usa apenas:
#    - listas simples
#    - if / elif / else
#    - operadores in / not in
#    - input + strip + lower
#
# 7. NÃO usar:
#    - funções
#    - dicionários
#    - listas avançadas
#    - nada além do que está no Capítulo 5
#
# Objetivo:
# Treinar validação de entrada, listas simples e estruturas condicionais.

cores = ['green', 'red', 'yellow']

print("A lista contém as cores:", cores)

escolha = input("Escolha uma das cores disponíveis na lista: ").strip().lower()

# Validação primeiro
if escolha not in cores:
    print("Opção inválida! Essa cor não está disponível.")
else:
    # Lógica do jogo
    if escolha == 'green':
        print('You earned 10 points and can destroy an alien!')
    elif escolha == 'red':
        print('You earned 500 points and now you can blast an alien!')
    elif escolha == 'yellow':
        print('You scored 80000 points and can take out an alien.')

# ===============================================================================================================
# ========================= OPÇÃO PARA CASO A COR NÃO FOSSE A CORRETA, VOLTAR A PEDIR? ==========================
# ===============================================================================================================

cores = ['green', 'red', 'yellow']

print("A lista contém as cores:", cores)

escolha = input("Escolha uma das cores disponíveis na lista: ").strip().lower()

# Enquanto a escolha NÃO estiver na lista, repete
while escolha not in cores:
    print("Opção inválida! Essa cor não está disponível.")
    escolha = input("Escolha novamente uma cor válida: ").strip().lower()

# Quando sair do while, a cor é válida
if escolha == 'green':
    print('You earned 10 points and can destroy an alien!')

elif escolha == 'red':
    print('You earned 500 points and now you can blast an alien!')

elif escolha == 'yellow':
    print('You scored 80000 points and can take out an alien.')


