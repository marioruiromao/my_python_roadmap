


apagar = 0          # MUITO IMPORTANTE: FICA FORA PORQUE VAI ACUMULANDO.
                    # 'apagar' é um ACUMULADOR.
                    # Ele precisa de lembrar o total das compras ao longo de TODAS as voltas do while.
                    # Por isso tem de ser inicializado FORA do while.
                    # Se estivesse DENTRO, seria REINICIADO a 0 em cada iteração e nunca acumularia nada.

while True:         # Este while repete o processo até o utilizador digitar 0.
    codigo = int(input("Código da mercadoria (0 para sair): "))
    preco = 0       # 'preco' é uma VARIÁVEL TEMPORÁRIA.
                    # Só serve para guardar o preço do produto desta iteração, nada mais.
                    # Não preciso do valor anterior, por isso posso (e devo) inicializá-la aqui.
                    # Cada volta do while começa com "preco = 0" NOVO, e isso é exatamente o que eu quero.
    if codigo == 0:
        # Se o utilizador digitar 0, o programa termina.
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
        print("Código inválido!")      # Como o código é inválido, não devo pedir quantidade nem somar nada. Uso 'continue' para saltar para a próxima volta do while.
        continue

    # Se cheguei aqui, o código é válido e 'preco' já tem o valor correto.

    quantidade = int(input("Quantidade: "))         # A quantidade é pedida apenas quando o código é válido.

    apagar += preco * quantidade
                                                    # Aqui estou a usar o valor ATUAL de 'preco' multiplicado pela quantidade.
                                                    # 'apagar' acumula o total, por isso está fora do while.
                                                    # Se estivesse dentro, seria sempre 0 e nunca somaria nada.

    print(f"Total a pagar {apagar:8.2f}€")
    # Mostro o total


    # ================================================================================================================================
    # ============================================ RESOLUÇÃO DO NILO MENEZES =========================================================
    # ================================================================================================================================

##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2024
# Quarta Edição - Março/2024 - ISBN 978-85-7522-886-9
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: capitulo 05/exercicio-05-15.py
##############################################################################
apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair): "))
    preço = 0
    if código == 0:
        break
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")