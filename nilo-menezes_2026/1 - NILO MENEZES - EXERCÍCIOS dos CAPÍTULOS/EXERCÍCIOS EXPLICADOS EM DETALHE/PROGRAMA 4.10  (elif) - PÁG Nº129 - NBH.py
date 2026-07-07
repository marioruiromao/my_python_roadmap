# Reescrever o Prob 4.8 da operadora Tchau usando o "elif"

#    Dados:
# PLANO FALO POUCO: 100 minutos, preço 50€, minutos extra 0.20€/minuto.
# PLANO FALO MUITO: 500 minutos, preço 99€, minutos extra 0.15€/minuto.

#    Problema:
# Um programa que pergunte o plano e a quantidade de minutos consumida e depois
# calcular o preço a pagar. Se não for nenhum plano, não se calcula o preço.
# _______________________________________________________________________________


# RESOLUÇÃO

# Pedimos o tarifário ao utilizador
tarifario = input("Qual é o tarifário móvel que tem? ")

# Normalizamos o texto:
# .lower()  → tudo em minúsculas
# .strip()  → remove espaços no início e no fim
# .replace(" ", "") → remove espaços internos
tarifario = tarifario.lower().strip().replace(" ", "") #Esta ordem deve ser respeitada

valido = True #Boa prática!

# Inicialização das variáveis (boa prática)
minutos_do_tarifario = 0
minutos_extra = 0
preco = 0

# Verificação do tarifário já normalizado
if tarifario == "falapouco":
    minutos_do_tarifario = 100
    minutos_extra = 0.20
    preco = 50

elif tarifario == "falamuito":
    minutos_do_tarifario = 500
    minutos_extra = 0.15
    preco = 99

else:
    valido = False

if not valido:
    print(f"Erro: não conheço o tarifário introduzido.")

else:
    minutos_consumidos = int(input("Quantos minutos gastou? "))
    suplemento = 0
# NBH:
# O que o utilizador escreve vem sempre como string (texto), mesmo que ele escreva 150. Exemplo: Se o utilizador escrever 120, 
# o valor de retorno é "120" (string). O int(...) vai converter essa string num número inteiro. Ou seja: "120" → 120.
# NBH:
# Porquê começar em 0? Aqui a ideia é mais de lógica e segurança do que de cálculo imediato. O suplemento é o valor extra a pagar,
# se o cliente ultrapassar os minutos incluídos no tarifário. Mas pode acontecer que ele não ultrapasse os minutos, e neste caso não há "suplemento"

    if minutos_consumidos > minutos_do_tarifario:
        suplemento = minutos_extra * (minutos_consumidos - minutos_do_tarifario)

    total = preco + suplemento

    print(f"Suplemento: {suplemento:.2f}€")
    print(f"Total a pagar: {total:.2f}€")


