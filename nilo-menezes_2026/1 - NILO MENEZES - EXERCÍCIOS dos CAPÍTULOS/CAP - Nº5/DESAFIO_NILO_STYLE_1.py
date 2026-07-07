#🔥 Desafio — Contagem com Mensagens Especiais
#🎯 Objetivo
#Criar um programa em Python que treine:
#Ciclos while
#Condições dentro do ciclo
#Ordem correta das instruções

#Indentação (o coração do Python)

#🧩 Enunciado
#Escreve um programa que: Começa em 10 e conta até 0

# Durante a contagem:

# Quando o número for 5, imprime também: "Metade do caminho!"
# Quando o número for 2, imprime também: "Quase lá!"
# Quando chegar a 0, imprime apenas no fim: "Fogo!"


# RESOLUÇÃO: -----------------------------------------------

x = 10
while x >= 0:
    print(x)
    if x == 5:
        print("Metade do percurso!")
    if x == 2:
        print("Quase lá")
    x = x - 1 # Se queres que a mensagem esteja ligada ao número que aparece no ecrã, faz o "if" antes de alterar "x"
print("fogo!")
    



