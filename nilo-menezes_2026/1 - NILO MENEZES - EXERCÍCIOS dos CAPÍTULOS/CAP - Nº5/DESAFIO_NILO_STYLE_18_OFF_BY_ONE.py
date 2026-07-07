# ============================================================
# EXERCÍCIO — SIMULAÇÃO DE EMPRÉSTIMO (Versão 3 de 3)
# Mês começa em 1, mas o incremento acontece no INÍCIO do ciclo
# Capítulo 5 — Nilo Menezes
# ============================================================

# Escreva um programa que simule o pagamento de um empréstimo.

# O programa deve:

# 1. Pedir ao utilizador:
#    - o valor inicial do empréstimo
#    - a taxa de juro mensal (%)
#    - o valor que será pago mensalmente

# 2. A cada mês, o programa deve:
#    - incrementar o número do mês logo no INÍCIO do ciclo
#    - calcular o valor dos juros do mês
#    - somar os juros ao saldo
#    - subtrair o pagamento mensal
#    - mostrar o número do mês, os juros cobrados e o saldo atualizado

# 3. O programa deve continuar enquanto o saldo for maior que zero.

# 4. Se o saldo ficar negativo, deve ser ajustado para zero.

# 5. No final, o programa deve mostrar:
#    - quantos meses foram necessários para pagar o empréstimo
#    - o total pago apenas em juros

# Nesta VERSÃO 3:
# - A contagem dos meses começa em 1.
# - O incremento do mês acontece no INÍCIO do while.
# - Isto altera completamente a lógica e é a versão mais propensa
#   ao erro clássico de “off-by-one”.

#____________________________________RESOLUÇÃO___________________________________________________________________

emprestimo = float(input('Diga o valor do seu empréstimo (€)? '))
taxa = float(input('Diga a taxa de juro (%) que vai pagar? '))
mensalidade = float(input('Diga quanto irá pagar por mês (€)? '))

mes = 0             # Ver NOTA 1ª. Explicação em baixo.
saldo = emprestimo
total_juros = 0

while saldo > 0:
    mes += 1
    juros_mensais = saldo * taxa / 100
    saldo += juros_mensais
    saldo -= mensalidade
    total_juros += juros_mensais

    if saldo < 0:
        saldo = 0

    print(f'Mês: {mes:4d} || Os juros cobrados: {juros_mensais:7.2f}€ || O saldo atualizado é: {saldo:8.2f}€ ')

print(f'Foram precisos {mes:4d} meses para pagar o empréstimo')     # NOTA 2ª, ver explicação do meu ERRO
print(f'O total de juros foi {total_juros:8.2f}€ ')

# EXPLICAÇÕES:
# NOTA 1ª - cOMO quero que o primeiro mês mostrado seja o mês 1, mas o incremento do mês acontece NO INÍCIO do while.
# Assim, para o primeiro mês ser 1, tenho de começar em 0. Se eu começasse em 1 e incrementasse logo no início, 
# o primeiro mês mostrado seria 2 (mes = 0)

# NOTA 2ª - Como comecei em 0 e fui incrementando NO INÍCIO do ciclo, o valor de "mes" neste ponto já é exatamente o número de meses usados.
# No meu código original eu tinha "mes - 1", o que aqui seria um erro de off-by-one.