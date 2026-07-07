
# Nível 2 — Contar uns, Somar outros

# Lê vários números inteiros.
# O programa termina quando o utilizador digitar 0.
#
# Durante a leitura:
#   - Conta quantos números POSITIVOS foram digitados (CONTADOR)
#   - Soma apenas os números NEGATIVOS (ACUMULADOR)
#
# No final, mostra:
#   - Quantidade de positivos
#   - Soma dos negativos


#      SOLUÇÃO: 

contador_positivo = 0
soma_negativa = 0

while True:
    numero = int(input('Digite os numeros inteiros que desejar. Quando quiser para digite"0":  '))
    if numero == 0:
        break
    if numero > 0:
        contador_positivo += 1
    elif numero < 0:            # Não uso 'else' porque significa: “qualquer coisa que não seja positiva”. Mas tu queres algo mais específico: “somente números negativos
        soma_negativa += numero

print(f'Os números positivos são: {contador_positivo} ')
print(f'A soma dos negativos é: {soma_negativa} ')
    

# NOTA -  O 'else' significa: “qualquer coisa que não seja positiva”, mas eu quero algo mais específico: “somente números negativos”. Quando é que poderias usar else?
#          Podia usar else se só existissem duas possibilidades: positivo ou negativo. Mas no teu programa existe uma terceira: zero → parar
#          E como zero já foi tratado no if numeros == 0, então sobram duas possibilidades: positivo e negativo. 
# Neste caso, poderias escrever:
#   if numeros > 0:
#        contador += 1
#   else:
#       soma += numeros

