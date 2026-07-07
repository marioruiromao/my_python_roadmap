# Quero ler vários números inteiros do utilizador.
# Somar todos, contar quantos foram digitados
# e no fim mostrar: quantidade, soma e média.

soma = 0            # soma → acumula os valores digitados
quantidade = 0      # quantidade → conta quantos números foram digitados

while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))        # Leio um número inteiro do utilizador, e se for 0, significa que o utilizador quer terminar.

    if numero == 0:
        break         # break → sai imediatamente do ciclo while

    soma += numero         # Adiciono o número à soma total
    quantidade += 1        # Conto mais um número digitado

# Quando o ciclo termina, posso calcular a média.
# Mas só posso dividir se quantidade > 0.

if quantidade > 0:
    media = soma / quantidade       # Média = soma dos números / quantidade de números
else:
    media = 0          # Se nenhum número foi digitado, evito divisão por zero.

print(f'Quantidade: {quantidade}')        # Mostro quantos números foram digitados
print(f'Soma: {soma}')                    # Mostro a soma total
print(f'Média: {media}')                  # Mostro a média calculada


# ------------------------------------ RESOLUÇÃO DO NILO MENEZES-------------------------------------------------------------------------------------

# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2024
# Quarta Edição - Março/2024 - ISBN 978-85-7522-886-9
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: capitulo 05/exercicio-05-14.py
##############################################################################
soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:10.2f}")