# EXERCÍCIO 5.15

# Solicitar ao usuário que digite o código do produto (Tabela) e a quantidade comprada.
# o programa deve:
#               1 - Exibir o total de compras depois do usuário digitar '0':
#               2 - Qualquer outro código deve originar "Código Inválido"
#
# Código:   1  -  2  -  3   -  5  -  9
# PREÇO:  0.5 - 1,00 - 4,00 - 7,00 - 8,00 


# Exercício 5.15 NEW_VERSION

total_compras = 0

while True:
    codigo_produto = int(input('Digite o código do produto que vai comprar! Para terminar digite "0": '))
    preco = 0           # MTO IMPORTANTE: Fica dentro WT, porque é uma variável utilizada apenas quando usamos o "codigo_produto", depois é limpa e volta a ser ZERO

    if codigo_produto == 0:
            break
    
    if codigo_produto == 1:
            preco = 0.50
    elif codigo_produto == 2:
            preco = 1.00
    elif codigo_produto == 3:
            preco = 4.00
    elif codigo_produto == 5:
            preco = 7.00
    elif codigo_produto == 9:
            preco = 8.00
    else:
            print('Erro! Código inválido!')
            continue # Posso usar também, na mesma posição, "if codigo_produto != 0" (NT - VER RESOLUÇÃO DO NILO MENEZES)
    
    quantidade = float(input('Digite o valor da quantidade comprada: '))

    quantidade_comprada = quantidade * preco
    total_compras += quantidade_comprada
    
print(f'O total de compras a pagar é:{total_compras:8.2f}€')