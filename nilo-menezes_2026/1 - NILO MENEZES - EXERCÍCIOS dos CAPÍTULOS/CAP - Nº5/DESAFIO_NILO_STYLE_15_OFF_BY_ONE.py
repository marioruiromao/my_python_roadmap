# ============================================================
# EXERCÍCIO — SIMULAÇÃO DE EMPRÉSTIMO (  Versão 1:  "Off-by-One"  )
# Contagem de meses começando em 1
# Capítulo 5 — Nilo Menezes
# ==================================================================

# Escreva um programa que simule o pagamento de um empréstimo.

# O programa deve:

# 1. Pedir ao utilizador:
#    - o valor inicial do empréstimo
#    - a taxa de juro mensal (%)
#    - o valor pago mensalmente

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

# Regras:
# - Usar apenas conteúdo do Capítulo 5:
#   variáveis, input, float, while, acumuladores e print.
# - Não usar funções, listas, break ou estruturas avançadas.
# - Nesta VERSÃO 1, o mês deve começar em 1.


# RSOLUÇÃO:____________________________________________________________________

valor_inicial = float(input('Qual é o valor inicial do seu empréstimo(€)? '))
taxa = float(input('Qual é o valor a taxa de juro do seu empréstimo (%)? '))
valor_mensal = float(input('Quanto é que vai pagar por mês(€)? '))

mes = 1                     # É uma instrução de atribuição
saldo = valor_inicial       # O saldo começa igual ao valor inicial do empréstimo. Não acumula valores, apenas muda ao longo do tempo. Nome técnico: variável de estado
total_juros = 0             # O 'Acumulador' porque serve para somar todos os juros pagos ao longo do tempo

while saldo > 0:
    juros_mes = saldo * taxa / 100          # Os juros são sempre calculados sobre o saldo da dívida, nunca sobre o pagamento mensal. juros_mes → VARIÁVEL TEMPORÁRIA Calculado do zero a cada mês. Não depende do valor anterior.
    total_juros = total_juros + juros_mes   # total_juros → ACUMULADOR Guarda a soma total dos juros ao longo do tempo.
    saldo += juros_mes                      # saldo → VARIÁVEL DE ESTADO Representa o valor atual da dívida. É atualizado (sobe/desce), não acumulado.
    saldo = saldo - valor_mensal  

    if saldo <= 0:                          # temos que o colocar antes do print(), senão aparecem valores negativos.
        saldo = 0

    print(f'O mês é: {mes:2d} || Os juros cobrados são: {juros_mes:4.2f}€ || O saldo é: {saldo:9.2f}€')
    mes += 1
   

print(f'\nForam necessários {mes - 1:2d}meses para pagar o empréstimo')
print(f'Foram pagos no juros no total {total_juros:7.2f}€')


# ============================================================
# ANÁLISE TÉCNICA DA EXPRESSÃO:
#     total_juros = total_juros + juros_mes
# ============================================================

# total_juros  → variável (lado esquerdo da atribuição, "l-value")
# =            → operador de atribuição (significa "recebe", não "igual a")
# total_juros  → variável (lado direito da atribuição, "r-value")
# +            → operador aritmético de adição
# juros_mes    → variável cujo valor será somado ao acumulador

# Nome técnico da linha inteira:
# → expressão de acumulação (acumulador)
# → padrão de atualização incremental

# Versão equivalente em Python (atribuição composta):
# total_juros += juros_mes
# Aqui "+=" é o operador de atribuição composta: soma e atribui.






