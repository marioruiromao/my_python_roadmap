# ENUNCIADO DO EXERCÍCIO (Capítulo 5 - Nilo Menezes)
# ---------------------------------------------------
# Escreva um programa que:
#
# 1. Peça ao utilizador:
#    - o valor inicial da dívida
#    - a taxa de juro mensal (%)
#    - o pagamento mensal
#
# 2. A cada mês, o programa deve:
#    - calcular os juros do mês
#    - somar os juros ao saldo
#    - subtrair o pagamento mensal
#    - mostrar o mês, os juros e o saldo atualizado
#
# 3. O programa deve continuar enquanto a dívida for maior que zero.
#
# 4. No final, o programa deve mostrar:
#    - quantos meses demorou a pagar a dívida
#    - quanto foi pago apenas em juros
#
# Regras:
# - Usar apenas conteúdo do Capítulo 5:
#   variáveis, input, float, while, acumuladores e print.
# - Não usar funções, listas, break ou estruturas avançadas.

#========================================================================================================

divida = float(input('Digite o valor em divída: '))
taxa = float(input('Qual é a sua taxa (%) de juro? '))
amortizacao = float(input('Quanto vai pagar mensalmente? '))

mes = 1
saldo = divida

while saldo > 0:
    juro = saldo * taxa / 100
    saldo += juro
    saldo -= amortizacao

    if saldo < 0:
        saldo = 0   # Evito saldo negativo no último mês.
 
    print(f'O mês é {mes:2d} || Os juros são: {juro:4.2f}€ || O seu saldo é de {saldo:7.2f}€ ')
    mes += 1

print(f'Demorou {mes} meses a pagar a divida')    # Estes prints agora estão FORA do while. Só aparecem quando o ciclo termina. 
print(f'Pagou {juro}€ juros de divida ')


# OUTRA VERSÃO COM "WHILE TRUE"============================================================================

divida = float(input('Digite o valor em divída: '))
taxa = float(input('Qual é a sua taxa (%) de juro? '))
amortizacao = float(input('Quanto vai pagar mensalmente? '))

mes = 1
saldo = divida

while True:    # Este ciclo vai repetir para sempre... até eu usar break.
    juro = saldo * taxa / 100
    saldo += juro
    saldo -= amortizacao

    if saldo < 0:
        saldo = 0
        # Evito saldo negativo.

    print(f"Mês {mes:2d} | Juros: {juro:6.2f}€ | Saldo: {saldo:7.2f}€")
    mes += 1

    if saldo == 0:  # Quando a dívida chega a zero, mando parar o ciclo.
        break

