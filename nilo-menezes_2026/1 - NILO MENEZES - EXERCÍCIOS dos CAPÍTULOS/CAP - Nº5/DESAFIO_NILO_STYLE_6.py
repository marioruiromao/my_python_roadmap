
# DESAFIO: Detectar padrões com módulo

# 1. Começa em 1
# 2. Conta até 50
# 3. Em cada número:
#    - Se for múltiplo de 4 → "→ Múltiplo de 4"
#    - Se for múltiplo de 6 → "→ Múltiplo de 6"
#    - Se for múltiplo de 4 e 6 → "🔥 SUPER múltiplo (4 e 6)"
#    - Se o resto da divisão por 5 for 2 → "Resto 2 quando dividido por 5"
# 4. No fim → "Fim da análise de módulo!"


#RESOLUÇÃO:---------------------------------------------------------------

x = 1

while x <= 50:
    print(x)

    if x % 4 == 0:
        print('Múltiplo de 4')

    if x % 6 == 0:
        print('Múltiplo de 6')

    if x % 4 == 0 and x % 6 == 0:
        print('SUPER MÚLTIPLO (4 e 6)')

    if x % 5 == 2:
        print('Resto 2 quando dividido por 5')

    x = x + 1  # E está no fim da iteração, que é exatamente onde deve estar, isto garante: primeiro uso o
               # valor atual e depois avanças para o próximo

print('Fim de análise de módulo')

# NUNCA ME ESQUECER: 1 - A ordem dos if só importa quando uma condição depende da outra.
#                    2 - Se forem independentes, posso colocá‑las na ordem que quiseres.  
