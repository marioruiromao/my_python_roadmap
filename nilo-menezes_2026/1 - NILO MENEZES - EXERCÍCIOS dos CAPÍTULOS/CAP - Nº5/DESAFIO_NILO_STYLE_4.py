
# DESAFIO: Contagem decrescente com alertas especiais

# 1. Começa em 50
# 2. Conta até 0
# 3. Em cada número:
#    - Se for múltiplo de 10 → "⚠️ Atenção: múltiplo de 10!"
#    - Se for múltiplo de 7 → "→ Número especial (múltiplo de 7)"
#    - Se for menor que 5 → "🚨 Últimos números!"
# 4. No fim → "Fim da missão!"


# --------------------------------RESOLUÇÃO--------------------------------

x = 50

while x >= 0:
   
    print(x)
    if x % 10 == 0: # NT - É o % (resto) que devemos usar!
        print('Atenção: múltiplo de 10!') 
    if x % 7 == 0:
        print('Número especial - múltiplo de 7!')
    if x < 5:
        print('Últimos números!')
    x = x - 1
    
print('Fim da emissão!')

# NO CASO DE QUERER QUE AS MENSAGENS APAREÇAM ANTES DOS NÚMERO!

x = 50

while x >= 0:

    # Mensagens primeiro
    if x % 10 == 0:
        print("⚠️ Atenção: múltiplo de 10!")

    if x % 7 == 0:
        print("→ Número especial (múltiplo de 7)")

    if x < 5:
        print("🚨 Últimos números!")

    # Só depois mostramos o número
    print(x)

    x = x - 1

print("Fim da emissão!")
