

# EXERCÍCIO — Gerar os primeiros N números perfeitos
#
# Um número perfeito é um número cuja soma dos seus divisores próprios
# (excluindo ele mesmo) é igual ao próprio número.
#
# Exemplos:
# 6  → 1 + 2 + 3 = 6
# 28 → 1 + 2 + 4 + 7 + 14 = 28
#
# Escreva um programa que:
#
# 1) Leia um valor inteiro N, representando quantos números perfeitos
#    devem ser numeros_gerados.
#


# ====== RESOLUÇÃO ======


quantidade = int(input("Quantos números perfeitos deseja gerar? ")) # Lê do utilizador quantos números perfeitos devem ser numeros_gerados

if quantidade <= 0:
    print("Erro! Digite um valor positivo.")
else:
    numeros_gerados = 0     # é um CONTADOR
    numero_perfeito = 2     # começamos com 2 porque 1 não é considerado número perfeito
    
    while numeros_gerados < quantidade:
        soma = 0
        divisor = 1

  
        while divisor < numero_perfeito:
            if numero_perfeito % divisor == 0:
                soma = soma + divisor
                divisor = divisor + 1

            if soma == numero_perfeito:
                print(numero_perfeito)
                numeros_gerados = numeros_gerados + 1

        numero_perfeito = numero_perfeito + 1
       


# ====== RESOLUÇÃO PROPOSTA ======

# EXERCÍCIO — Gerar os primeiros N números perfeitos
# CAPÍTULO 5 — Nilo Menezes
# Objetivo: praticar while, if, contadores, acumuladores e uso de divisores.
quantidade = int(input("Quantos números perfeitos deseja gerar? ")) # Lê do utilizador quantos números perfeitos devem ser numeros_gerados
# 1) Primeiro tratamos os casos especiais:
#    Se a quantidade for menor ou igual a zero, não faz sentido continuar.
if quantidade <= 0:
    print("Erro! Digite um valor positivo.")
# 2) Caso geral: quando a quantidade é positiva, vamos procurar números perfeitos.
else:
    # 'numeros_gerados' é um CONTADOR.
    # Vai guardar quantos números perfeitos já encontramos e mostramos.
    numeros_gerados = 0
    # 'numero_perfeito' é o número que vamos testar para ver se é perfeito.
    # Começamos em 2, porque 1 não é considerado número perfeito.
    numero_perfeito = 2
    # Enquanto ainda não tivermos gerado a quantidade pedida, continuamos a procurar.
    while numeros_gerados < quantidade:
        # 'soma' é um ACUMULADOR.
        # Vai somar todos os divisores próprios de 'numero_perfeito' (excluindo ele mesmo).
        soma = 0

        # 'divisor' começa em 1, porque todo número é divisível por 1.
        divisor = 1

        # Este while vai testar todos os possíveis divisores menores que 'numero_perfeito'.
        while divisor < numero_perfeito:
            # Se o resto da divisão de 'numero_perfeito' por 'divisor' for zero,
            # então 'divisor' é um divisor próprio de 'numero_perfeito'.
            if numero_perfeito % divisor == 0:
                # Somamos esse divisor ao acumulador 'soma'.
                soma = soma + divisor

            # Passamos para o próximo possível divisor.
            divisor = divisor + 1

        # Quando o while interno termina, 'soma' contém a soma de todos
        # os divisores próprios de 'numero_perfeito'.
        # Se essa soma for igual ao próprio 'numero_perfeito', então ele é perfeito.
        if soma == numero_perfeito:
            # Mostramos o número perfeito encontrado.
            print(numero_perfeito)

            # Atualizamos o contador de números perfeitos numeros_gerados.
            numeros_gerados = numeros_gerados + 1

        # Independentemente de ser perfeito ou não, avançamos para o próximo número.
        numero_perfeito = numero_perfeito + 1

        
        




