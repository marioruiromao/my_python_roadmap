# ENUNCIADO DO EXERCÍCIO (Capítulo 5 - Nilo Menezes)
# ---------------------------------------------------
# Escreva um programa que simule o pagamento de um empréstimo.
#
# O programa deve:
#
# 1. Pedir ao utilizador:
#    - o valor inicial do empréstimo
#    - a taxa de juro mensal (%)
#    - o valor que será pago mensalmente
#
# 2. A cada mês, o programa deve:
#    - calcular o valor dos juros do mês
#    - somar os juros ao saldo
#    - subtrair o pagamento mensal
#    - mostrar o número do mês, os juros cobrados e o saldo atualizado
#
# 3. O programa deve continuar enquanto o saldo for maior que zero.
#
# 4. Se o saldo ficar negativo, deve ser ajustado para zero.
#
# 5. No final, o programa deve mostrar:
#    - quantos meses foram necessários para pagar o empréstimo
#    - o total pago apenas em juros
#
# Regras:
# - Usar apenas conteúdo do Capítulo 5:
#   variáveis, input, float, while, acumuladores e print.
# - Não usar funções, listas, break ou estruturas avançadas.

#========================================= RESOLUÇÃO ================================================================

divida = float(input('Digite o valor do seu empréstimo (€)? '))
taxa = float(input('Qual é a sua taxa de juro (%)? '))  # Taxa fixa de juro (ex: 3%). NÃO será alterada!
amortizacao = float(input('Quanto irá amortizar mensalmente (€)? '))

mes = 1
saldo = divida
total_juros = 0     # NBH - Acumulador para somar todos os juros pagos.


while saldo > 0:    # Loop principal
    juros_mes = saldo * taxa / 100      # Cálculo dos juros do mês. Agora usamos 'juros_mes' e NÃO destruímos a variável 'taxa'
    saldo = saldo + juros_mes
    saldo = saldo - amortizacao
    total_juros += juros_mes   # Acumula os juros pagos, indo buscar a do mês anterior e somando com os do mês atual.

    if saldo < 0:   # Evita saldo negativo
        saldo = 0

    print(f'Mês {mes:2d} || Juros: {juros_mes:7.2f}€ || Saldo: {saldo:8.2f}€')
    mes += 1
 
print(f'\nForam precisos {mes-1} meses para pagar o empréstimo.')       # NBH - 'mes-1' porque o último incremento acontece depois do pagamento
print(f'Total pago apenas em juros: {total_juros:.2f}€')                # Mostra o total acumulado de juros

# ____________________________________________________________________SUPER IMPORTA__________________________________________________________________
#  Onde é que o mês é incrementado?

# No teu ciclo tens algo deste género: quando o ciclo acaba, o mês já está “um mês à frente”. Por isso, para dizer quantos meses realmente aconteceram, 
# tens de recuar um: mes - 1.

# Como evitar isso (só para cultura geral)

# Há duas abordagens comuns:
#       1 - Começar mes em 0 e incrementar no início do ciclo: Assim, o valor de mes ao sair do ciclo já corresponde ao número de meses.
#       2 - Manter como está e usar mes - 1 no fim. Perfeitamente válido e muito comum. 
#       3 - Pedir no próximo EXERCÍCIO para mostrar três versões diferentes do mesmo programa, só a mudar a forma como contamos os meses, 
#           para treinares esta noção de “off-by-one” (erros de +1/−1), que é um clássico da programação.