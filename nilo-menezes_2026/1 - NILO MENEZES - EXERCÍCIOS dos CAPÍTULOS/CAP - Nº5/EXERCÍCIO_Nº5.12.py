
deposito_inicial = float(input('Digite o depósito que fez (€)? '))
taxa_juro = float(input('Qual é a taxa de juro (%)? '))
deposito_mensal = float(input('Qual é o valor mensal do seu depósito? '))

mes = 1
saldo = deposito_inicial

while mes <= 24:
    juros = saldo * taxa_juro / 100
    saldo += juros
    saldo += deposito_mensal  # entra o depósito mensal
    print(f'Mês {mes:2d} -- Juros: {juros:7.2f}€  --  Saldo: {saldo:8.2f}€')
    mes += 1  # Se ficar antes do print() o cálculo é do mês 1, mas o print mostra mês 2.

total_investido = deposito_inicial + deposito_mensal * 24 # Não está pedido no problema
ganho_juros = saldo - total_investido                     # Não está pedido no problema

print(f'Ganho total em juros: {ganho_juros:8.2f}€')

    


# NOTA MUITO IMPORTANTE =======================================================================================================================

# 1 - Não precisamos de colocar 'juros = 0' porque nunca é lido sem ter valor, nunca acumula valores e é sempre substituido por um novo cálculo.
#     A variável JUROS é sempre CALCULADA dentro do while ANTES de ser usada.

# 2 - Só colocamos uma variável quando precisamos de um valor inicial ANTES de a usares (ex: mes = 1)

# 3 - Se a variável recebe SEMPRE um valor antes de ser usada, não precisas de inicializar (ex: juros = 0).



# ========================= FEITO pelo NILO ===================================================================================================

depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal: "))

mês = 1
saldo = depósito

while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")
