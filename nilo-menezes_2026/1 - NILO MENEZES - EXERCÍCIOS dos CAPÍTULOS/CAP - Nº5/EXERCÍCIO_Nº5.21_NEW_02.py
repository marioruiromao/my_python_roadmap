
#  ENUNCIADO — Exercício Simplificado: Notas de 10€ e 5€

#  Escreva um programa que:
        #   1. Peça ao utilizador um valor_positivo inteiro positivo.
        #   2. O programa deve decompor esse valor_positivo usando apenas notas de 10€ e 5€.
        #   3. O programa deve mostrar quantas notas de 10€ e quantas notas de 5€ são necessárias.
        #   4. O programa deve repetir enquanto o utilizador não digitar 0.
        #   5. Ao digitar 0, o programa termina.





while True:  
    # Peço o valor ao utilizador. Aqui escrevo "valor" e não "valor_positivo"
    # porque o nome já deixa claro o suficiente.
    valor = int(input('Digite um valor inteiro positivo (0 para sair): '))

    # Se o valor for 0, termino o programa.
    if valor == 0:
        break

    # Aqui começo a decompor o valor.
    decompor = valor

    # Começo sempre pela nota de 10.
    nota_atual = 10

    # Contador de notas da nota_atual.
    quantidade_notas = 0

    while True:
        # Se ainda consigo tirar uma nota_atual do valor...
        if nota_atual <= decompor:
            # ...subtraio e aumento o contador.
            decompor -= nota_atual
            quantidade_notas += 1

        else:
            # Quando já não consigo tirar mais notas, mostro o total.
            print(f'Foram usadas {quantidade_notas} nota(s) de {nota_atual}€')

            # Se já não sobrar nada, termino o loop interno.
            if decompor == 0:
                break

            # Aqui mudo para a próxima nota.
            # O meu erro original era manter 10 → 10 e 5 → 5.
            # Isso fazia o loop ficar preso.
            if nota_atual == 10:
                nota_atual = 5

            # Reinicio o contador para a nova nota.
            quantidade_notas = 0

# RESUMO DE MESTRE:

# Como sei que preciso de condição aninhada?
# Quando uma decisão depende do resultado de outra decisão.

# Como identifico isso como programador?
# Quando o problema tem passos do tipo: “Se isto acontecer, então tenho de verificar aquilo.”

# Posso usar while em vez de while True?
# Sim, mas só quando tens uma única condição clara que controla o loop.

# Por que while True é melhor aqui?
# Porque o teu loop depende de várias decisões internas, não de uma condição simples.

# Muito importante: Visualiza como um “decidir dentro de decidir”

#       Pensa assim:
#   1 - Condição simples (não aninhada): Várias perguntas independentes, lado a lado.
#   2 - Condição aninhada: Fazes uma pergunta, entras num “corredor” (bloco de código), e lá dentro fazes outra pergunta.

    
