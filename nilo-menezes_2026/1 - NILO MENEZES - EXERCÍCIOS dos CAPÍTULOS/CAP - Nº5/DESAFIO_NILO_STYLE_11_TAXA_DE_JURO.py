#============================================================================================
#       PROBLEMA: Cria um programa que simule o crescimento de uma poupança mensal.
#=============================================================================================
# O programa deve pedir ao utilizador:
# - o valor inicial da poupança
# - o valor que deposita todos os meses
# - a taxa de juro mensal (em %)
# - o número total de meses a simular
#--------------------------------------------------------------------------------------------
# Usando um ciclo while, o programa deve calcular mês a mês:

# - o juro ganho naquele mês
# - o novo saldo após adicionar o depósito mensal e os juros
#--------------------------------------------------------------------------------------------
# Para cada mês, o programa deve mostrar:

# - o número do mês
# - o juro ganho
# - o saldo atualizado
#--------------------------------------------------------------------------------------------
# No final, o programa deve mostrar:

# - o total depositado pelo utilizador
# - o total de juros ganhos
# - o saldo final após todos os meses

# RESOLUÇÃO_________________________________________________________________________________

saldo_inicial = float(input('Valor da poupança inicial: '))
deposito_mensal = float(input('Depósito mensal: '))
taxa_juro = float(input('Qual é a taxa de juro mensal (em %)? '))
periodo_simulado = int(input('Período (em meses) que quer simular? '))

# Preparar variáveis
saldo = saldo_inicial          # saldo atual
mes = 1                        # contador de meses
total_juros = 0.0              # acumular juros ao longo do tempo

print('\n--- Simulação mês a mês ---')

while mes <= periodo_simulado:
    juros_mes = saldo * taxa_juro / 100     # calcular juros do mês sobre o saldo atual
    total_juros += juros_mes      # IMPORTANTE - É o acumular juros totais que vêem de trás (total_juros) mais (+) os do mês atual (juros_mes), depois guardado no total_juros
    saldo = saldo + juros_mes + deposito_mensal  # atualizar saldo: saldo anterior + juros + depósito mensal
    
    print(f'Mês {mes:2d}: juros = {juros_mes:7.2f}€, saldo = {saldo:8.2f}€')   # mostrar resultados do mês
    mes += 1   # é o que faz passar ao mês seguinte

# cálculos finais
total_depositado = saldo_inicial + deposito_mensal * periodo_simulado

print('\n--- Resumo final ---') # \n é um carácter especial que significa: “quebra de linha” (ou seja, “vai para a linha de baixo antes de imprimir o resto”). É como carregar no Enter no teclado.
print(f'Total depositado pelo utilizador: {total_depositado:8.2f}€')
print(f'Total de juros ganhos:           {total_juros:8.2f}€')
print(f'Saldo final após {periodo_simulado} meses: {saldo:8.2f}€')



