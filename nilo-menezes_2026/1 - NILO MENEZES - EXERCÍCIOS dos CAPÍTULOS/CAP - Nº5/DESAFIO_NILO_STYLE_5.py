# DESAFIO: Contagem decrescente com filtros inteligentes

# 1. Começa em 60
# 2. Conta até 0
# 3. Em cada número:
#    - Se for par → "→ Número par"
#    - Se for ímpar → "→ Número ímpar"
#    - Se for múltiplo de 5 → "⚠️ Divisível por 5!"
#    - Se estiver entre 20 e 10 → "Zona crítica!"
# 4. No fim → "Análise concluída!"

# RESOLUÇÃO:______________________________________

x = 60

while x >= 0:

    if x % 2 == 0: # nº par
        print('Número par!')
    if x % 2 != 0: # nº impar
        print('Número impar!')
    if x % 5 == 0:
        print('ATENÇÃO: divisível por 5!')
    if 10 < x < 20:
        print('zona crítica!')
    
    print(x)
    x = x -1
    
print('Análise concluida!')

