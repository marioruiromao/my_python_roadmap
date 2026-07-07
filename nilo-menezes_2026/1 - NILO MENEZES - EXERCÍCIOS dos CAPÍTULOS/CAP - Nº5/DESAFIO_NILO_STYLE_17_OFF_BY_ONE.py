# ============================================================
# EXERCÍCIO — SIMULAÇÃO DE EMPRÉSTIMO (Versão 2 de 3)
# Contagem de meses começando em 0
# Capítulo 5 — Nilo Menezes
# ============================================================

# Escreva um programa que simule o pagamento de um empréstimo.

# O programa deve:

# 1. Pedir ao utilizador:
#    - o valor inicial do empréstimo
#    - a taxa de juro mensal (%)
#    - o valor que será pago mensalmente

# 2. A cada mês, o programa deve:
#    - calcular o valor dos juros do mês
#    - somar os juros ao saldo
#    - subtrair o pagamento mensal
#    - mostrar o número do mês, os juros cobrados e o saldo atualizado

# 3. O programa deve continuar enquanto o saldo for maior que zero.

# 4. Se o saldo ficar negativo, deve ser ajustado para zero.

# 5. No final, o programa deve mostrar:
#    - quantos meses foram necessários para pagar o empréstimo
#    - o total pago apenas em juros

# Nesta VERSÃO 2:
# - A contagem dos meses começa em 0.
# - O incremento do mês acontece no INÍCIO do ciclo.
# - Isto altera a lógica e obriga a pensar no erro clássico de “off-by-one”.


# resolução: _________________________________________________________________________________

valor_emprestimo = float(input('Valor do empréstimo (€): '))
juros = float(input('Qual é a taxa de juros mensal(€)? '))
mensalidade = float(input('Quanto irá pagar por mês(€)? '))

mes = 0
saldo = valor_emprestimo
total_juros = 0

while saldo > 0:
    juros_mes = saldo * juros / 100
    saldo += juros_mes
    saldo -= mensalidade
    total_juros += juros_mes

    if saldo < 0:
        saldo = 0

    print(f'Mês: {mes:2d} // Juros cobrados: {juros_mes:5.2f}€ // O saldo: {saldo:10.2f}€ ')

    mes += 1

print(f'Foram necessários {mes:4d} meses para pagar o empréstimo ')
print(f'Pagou-se um total de {total_juros:4.2f}€ em juros ')

# LINHA 59 (LER ESTAS NOTAS) - Como comecei em 0 e incrementei no fim do ciclo, o valor de "mes" neste ponto já representa exatamente o número de meses usados.
# Por isso NÃO devo somar +1 (isso seria um erro de off-by-one).