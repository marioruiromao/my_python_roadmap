
#PROBLEMA: Perguntar o deposito inicial e a taxa de juro da poupança. Exiba os valores mês a mês, para os primeiros 24 meses, e depois o total ganho.

deposito_inicial = float(input('Qual é o valor do seu depósito inicial? '))  
taxa_juro = float(input('Qual é a porcentagem de juro mensal? '))             

mes = 1                                                                       
saldo = deposito_inicial                                                      
total_juros = 0.0    # Variável para acumular todos os juros ao longo dos 24 meses

while mes <= 24:                                                             
    juros_mes = saldo * taxa_juro / 100    # Calcula os juros daquele mês com base no saldo atual
    saldo += juros_mes     # Atualiza o saldo: saldo = saldo + juros do mês
    total_juros += juros_mes    # Soma os juros deste mês ao total de juros

    print(f'Mês {mes:2d}: juros = {juros_mes:8.2f}€, saldo = {saldo:8.2f}€') # Mostra o mês, os juros do mês e o saldo atualizado, tudo formatado
    mes += 1    # Avança para o próximo mês (mes = mes + 1). É o que faz avanças mês após mês até ao 24meses, por isso devo colocar sempre depois do print. 
                # Senão fazia o cálculo mas mostrava o mês2. Um sempre à frente.

print('=' * 50)   # Imprime uma linha de separação com 40 hífens. Apenas estética.
print(f'Depósito inicial: {deposito_inicial:8.2f}€')    # Mostra o depósito inicial formatado com 2 casas decimais, é para dar mais info.
print(f'Total de juros em 24 meses: {total_juros:8.2f}€')   # Mostra o total de juros acumulados nos 24 meses
print(f'Saldo final após 24 meses: {saldo:8.2f}€')  # Mostra o saldo final depois de 24 meses de capitalização


#========================================================================================
# O MEU código
#========================================================================================
deposito_inicial = float(input('Qual é o valor do seu depósito inicial? '))
taxa_juro = float(input('Qual é a porcentagem de juro mensal? '))

mes = 1
juros = 0

while mes <= 24:
    juros = deposito_inicial * taxa_juro/100
    mes += 1
    print(f'Os juros foram de {juros:8.2f}€ por mês. ')

print(f'O total de juros nos 24 meses foi de {24 * juros:8.2f}€ ')


##########################################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2024
# Quarta Edição - Março/2024 - ISBN 978-85-7522-886-9
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: capitulo 05/exercicio-05-11.py
##############################################################################
depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")
