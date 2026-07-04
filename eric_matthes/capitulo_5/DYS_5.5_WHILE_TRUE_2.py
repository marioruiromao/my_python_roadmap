# EXERCÍCIO — CAPÍTULO 5 (NILO MENEZES)
#
# Objetivo:
# Treinar ciclos while, validação de entrada e listas simples.
#
# ENUNCIADO:
#
# Cria um programa que peça ao utilizador para escolher um animal
# de uma lista simples com três opções:
#
#   - 'dog'
#   - 'cat'
#   - 'bird'
#
# 1. Mostra a lista ao utilizador.
#
# 2. Pede ao utilizador que escolha um animal.
#    - Usa strip() e lower() para normalizar a entrada.
#
# 3. Enquanto o utilizador NÃO escolher um animal válido,
#    o programa deve:
#       - Mostrar uma mensagem de erro
#       - Pedir novamente a escolha
#
# 4. Quando o utilizador finalmente escolher um animal válido,
#    mostra uma mensagem diferente para cada animal:
#
#       dog  → "Dogs are loyal!"
#       cat  → "Cats are independent!"
#       bird → "Birds can fly!"
#
# 5. Regras:
#    - Usa apenas listas simples
#    - Usa while para repetir até a escolha ser válida
#    - Usa if / elif / else para as mensagens finais
#    - Não usar funções, dicionários ou listas avançadas
#
# Objetivo final: Garantir que o utilizador só avança quando escolher um animal válido.

# =====================================================================================
#                                   RESOLUÇÃO
# =====================================================================================

lista_animais = ['dog', 'cat', 'bird']

print("Lista de animais disponíveis:", lista_animais)

escolha = input("Escolha um animal da lista: ").strip().lower()

while escolha not in lista_animais:
    print("Erro! Esse animal não existe na lista.")
    escolha = input("Escolha novamente um animal válido: ").strip().lower()

# Quando o while termina, a escolha é válida
if escolha == 'dog':
    print("Dogs are loyal!")
elif escolha == 'cat':
    print("Cats are independent!")
elif escolha == 'bird':
    print("Birds can fly!")
