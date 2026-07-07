##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2024
# Quarta Edição - Março/2024 - ISBN 978-85-7522-886-9
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: capitulo 05/exercicio-05-19.py

##############################################################################
# Atenção: alguns valores não serão calculados corretamente, devido a problemas com arredondamento e da representação de 0.01 em ponto flutuante. 
# Uma alternativa é multiplicar todos os valores por 100 e realizar todos os cálculos com números inteiros.


# PROGRAMA 5.1



# Peço o valor a pagar ao utilizador e converto para float,
# porque posso ter valores com casas decimais.
valor = float(input("Digite o valor a pagar: "))

# Contador de cédulas/moedas do valor atual.
cédulas = 0
# Começo pela maior cédula disponível.
atual = 100
# Valor que ainda falta decompor em cédulas/moedas.
apagar = valor

# Laço principal: vou repetir até que o valor restante seja muito pequeno.
while True:
    # Se a cédula/moeda atual ainda cabe no valor que falta apagar, subtraio e conto mais uma.
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        # Quando já não cabe, imprimo quantas cédulas/moedas deste valor usei.
        # Se o valor atual é pelo menos 1€, considero que é uma cédula (nota).
        if atual >= 1:
            print(f"{cédulas} cédula(s) de {atual}€")
        else:
            # Caso contrário, é uma moeda, e uso formatação com 2 casas decimais.
            print(f"{cédulas} moeda(s) de {atual:5.2f}€")

        # Se o que falta apagar é menor que 0.01€, paro o laço. Isto evita problemas de arredondamento com ponto flutuante.
        if apagar < 0.01:
            break

        # Caso ainda falte algum valor, avanço para a próxima cédula/moeda.
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01

        cédulas = 0  # Reinicio o contador de cédulas/moedas para o novo valor.

        # RESPOSTA:
        #
        # Conclusão clara e direta:

        # Quando digitO 0.001, o programa:
                # 1 - Não consegue subtrair nenhuma cédula/moeda, porque todas são maiores que 0.001.
                # 2 - Imprime 0 cédulas para cada valor.
                # 3 - Nunca chega à condição de paragem (apagar < 0.01).
                # 4 - Fica preso num ciclo, ou imprime tudo até ao fim e pára de forma estranha.
                # 5 - O algoritmo não funciona para valores tão pequenos.