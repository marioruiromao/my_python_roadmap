
# EXERCÍCIO 5.15

# Solicitar ao usuário que digite o código do produto (Tabela) e a quantidade comprada.
# o programa deve:
#               1 - Exibir o total de compras depois do usuário digitar '0':
#               2 - Qualquer outro código deve originar "Código Inválido"
#
# Código:   1  -  2  -  3   -  5  -  9
# PREÇO:  0.5 - 1,00 - 4,00 - 7,00 - 8,00 


# SOLUÇÃO: -------------------------------------------------------------------------------

# EXERCÍCIO 5.15 — Capítulo 5


apagar = 0      # MUITO IMPORTANTE: FICA FORA PORQUE VAI ACUMULANDO. O 'apagar' é um ACUMULADOR.
                # Ele precisa de lembrar o total das compras ao longo de TODAS as voltas do while.
                # Por isso tem de ser inicializado FORA do while.
                # Se estivesse DENTRO, seria REINICIADO a '0' em cada iteração e nunca acumularia nada.
while True:
    # Este while repete o processo até o utilizador digitar 0.

    codigo = int(input("Código da mercadoria (0 para sair): "))
    preco = 0           # 'preco' é uma VARIÁVEL TEMPORÁRIA. Só serve para guardar o preço do produto desta iteração.
                        # Não preciso do valor anterior, por isso posso (e devo) inicializá-la aqui.
                        # Cada volta do while começa com preco = 0, e isso é exatamente o que eu quero.
                        # Isto evita que um código inválido use o preço anterior por engano.
    if codigo == 0:
        break

    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!")               # Como o código é inválido, não devo pedir quantidade nem somar nada.
        continue                     # Uso 'continue' para saltar para a próxima volta do while.
        
    quantidade = int(input("Quantidade: "))     # A quantidade SÓ é pedida quando o código é válido.

    apagar += preco * quantidade                # Aqui estou a usar o valor ATUAL de 'preco' multiplicado pela quantidade.
                                                # 'apagar' acumula o total, por isso está FORA do while.
                                                # Se estivesse dentro, seria sempre '0' e nunca somaria nada.

    print(f"Total a pagar {apagar:8.2f}€")      # Mostro o total

    # NOTA IMPORTANTE: O print final tem de estar alinhado com o while.
    # Porque: 1) Tudo o que está dentro do while repete-se, 2) Tudo o que está fora do while só acontece uma vez, no fim.
    # 3) O alinhamento define o bloco de código.




# =========================================================================================================================== #
# VERSÃO PYTHONIC - MAIS AVANÇADA                                                                                             #
# =========================================================================================================================== #
precos = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00
}

total = 0

while True:
    codigo = int(input("Código do produto (0 para sair): "))

    if codigo == 0:
        break

    if codigo not in precos:
        print("Código inválido!")
        continue

    quantidade = int(input("Quantidade: "))
    total += precos[codigo] * quantidade

print(f"Total a pagar: {total:.2f}€")

