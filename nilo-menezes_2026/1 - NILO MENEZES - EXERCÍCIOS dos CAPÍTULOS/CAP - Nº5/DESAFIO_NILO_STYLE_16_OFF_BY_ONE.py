# ============================================================
# EXERCÍCIO — SIMULAÇÃO DE EMPRÉSTIMO (Versão 1 de 3)
# Contagem de meses começando em 1
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

# Nesta VERSÃO 1:
# - A contagem dos meses começa em 1.
# - Não é necessário ajustar com 'mes - 1' no final.

#-----------------------------------RESOLUÇÃO------------------------------------------

valor_inicial = float(input('Digite o valor inicial do empréstimo (€): '))
taxa = float(input('Qual é a sua taxa de juro mensal (%)'))
pagamento_mensal = float(input('Quanto irá pagar mensalmente (€)? '))

mes = 1
saldo = valor_inicial
taxa_total = 0

while saldo > 0:

    juro_mes = saldo * taxa / 100       # Os juros devem ser calculados sobre o saldo atual
    saldo += juro_mes
    saldo -= pagamento_mensal
    taxa_total += juro_mes

    if saldo < 0:
        saldo = 0
    
    print(f'O mês: {mes:2d} || Os juros mensais são: {juro_mes:5.2f}€ || O saldo é de: {saldo:10.2f}€ ')

    mes += 1
  
print(f'Foram precisos {mes:4d} meses para pagar o empréstimo ')
print(f'O valor total dos juros total foi de {taxa_total:9.2f}€ ')

