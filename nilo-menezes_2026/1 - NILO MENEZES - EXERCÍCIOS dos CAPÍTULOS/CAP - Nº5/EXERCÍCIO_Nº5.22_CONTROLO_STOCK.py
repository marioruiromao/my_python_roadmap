
# Exercício – Controle simples de stock

# Escreva um programa que:

# 1. Leia repetidamente o nome de um produto e sua quantidade em stock.

# 2. O programa deve parar quando o usuário digitar "fim" como nome do produto.

# 3. Após o término, o programa deve:

    #    - Mostrar quantos nome foram registados.
    #    - Exibir o nome do produto com a menor quantidade.
    #    - Exibir o total de itens no stock.
    #    - Exibir a média de itens por produto.



# RESOLUÇÃO:

# Contador de quantos produtos foram registados
quantidade_produtos = 0

# Acumulador do total de itens em stock
total_itens = 0

# Variável para guardar a menor quantidade encontrada. Começa como None para sabermos que ainda não temos valores (PÁG 187, 226, 235, 243, 369 e 383)
menor_quantidade = None 

# Nome do produto com menor quantidade
produto_menor = ""

while True:

    nome = input("Nome do produto (digite 'fim' para terminar): ")
    
    if nome == "fim":
        break

    quantidade = int(input("Quantidade em stock: "))
    
    quantidade_produtos += 1    # Atualiza o contador de produtos
    
    total_itens += quantidade   # Vai somando a quantidade ao total de itens

    # Verifica se esta é a menor quantidade registada até agora
    # 1º caso: menor_quantidade ainda é None → primeiro produto
    # 2º caso: quantidade atual é menor que a menor registada
    if menor_quantidade is None or quantidade < menor_quantidade:
        menor_quantidade = quantidade
        produto_menor = nome

# Impressão dos resultados finais
print("\n--- RESULTADOS ---")

# Quantos produtos foram registados

