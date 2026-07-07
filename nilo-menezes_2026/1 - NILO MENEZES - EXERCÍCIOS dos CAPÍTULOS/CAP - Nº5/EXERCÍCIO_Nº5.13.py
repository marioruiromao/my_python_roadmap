
divida = float(input('Qual é o valor inicial da sua dívida? '))
taxa = float(input('Qual é a taxa de juro mensal (%): '))   # Taxa de juro em percentagem. Evitar confusões.
amortizacao = float(input('Quanto irá pagar mensalmente? '))    # Pagamento fixo mensal. Este valor será subtraído todos os meses.

mes = 1
saldo = divida # O saldo deve começar igual à dívida inicial.

while saldo > 0:                        # O ciclo deve continuar enquanto ainda houver dívida.
    juros_mes = saldo * taxa / 100      # Calculo os juros do mês com base no saldo atual. Fundamental: juros variam conforme o saldo diminui.
    saldo += juros_mes                  # Primeiro adiciono os juros ao saldo. A dívida aumenta antes de eu pagar.
    saldo -= amortizacao                # Agora subtraio o pagamento mensal. Reduzo a dívida.
    if saldo < 0:
        saldo = 0                       # Evito mostrar saldo negativo no último mês.
    print(f"Mês {mes:2d} || Juros: {juros_mes:8.2f}€ || Saldo: {saldo:8.2f}€")  # Mostro o que aconteceu neste mês.
    mes += 1                            # Avanço para o próximo mês.
