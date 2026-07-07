# OS PASSOS LÓGICOS (a ponte entre história e código)

# Transformar a história em regras:

# Regra 1:
#       Enquanto o valor não for 0 → continua.
# Regra 2:
#       Começa sempre pela maior nota.
# Regra 3:
#       Enquanto a nota couber no valor → subtrai e conta.
# Regra 4:
#       Quando a nota já não couber → imprime e muda para a próxima.
# Regra 5:
#       Quando o valor chegar a 0 → termina.


while True:                 # Regra 1
    valor = int(input("Digite o valor a pagar! E '0' para sair: "))
    if valor == 0:
        break

    a_pagar = valor
    nota_atual = 50         # Regra 2
    notas_usadas = 0

    while True:
        if nota_atual <= a_pagar:  # Regra 3
            a_pagar -= nota_atual
            notas_usadas += 1
        else:  # Regra 4
            print(f"{notas_usadas} nota(s) de {nota_atual}€")
            if a_pagar == 0:  # Regra 5
                break

            if nota_atual == 50:
                nota_atual = 20
            elif nota_atual == 20:
                nota_atual = 10
            elif nota_atual == 10:
                nota_atual = 5
            elif nota_atual == 5:
                nota_atual = 1

            notas_usadas = 0

# -----------------------A VERSÃO FEITA COM LISTAS---------------------------------

notas = [50, 20, 10, 5, 1]  # Lista com todas as notas disponíveis

while True:
    valor = int(input("Digite o valor a pagar (0 para sair): "))

    if valor == 0:
        break

    a_pagar = valor

    for nota in notas:  # percorro cada nota da lista
        quantidade = a_pagar // nota  # quantas notas desta cabem no valor
        if quantidade > 0:
            print(f"{quantidade} nota(s) de {nota}€")
        a_pagar = a_pagar % nota  # atualizo o valor restante

    print()  # só para separar visualmente



