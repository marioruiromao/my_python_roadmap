
# DESAFIO: Classificação de Números com Contagem Decrescente
# OBJECTIVO: Criar um programa que usa um ciclo while e condições if/elif/else.

# Enunciado: ---------------------------------------------------------------------
# 1. O programa deve começar com o valor 20.
# 2. Deve fazer uma contagem decrescente até 0.
# 3. Para cada número:
#       - Se for par, imprimir: "X é par"
#       - Se for ímpar, imprimir: "X é ímpar"
#       - Se for múltiplo de 4, imprimir também: "Múltiplo de 4!"
# 4. Quando o número ficar negativo, o programa deve parar (não imprimir nada).
# 5. No fim da contagem, imprimir apenas uma vez: "Fim da classificação!"

# Notas importantes:
# - Usa if, elif e else dentro do ciclo.
# - A verificação de múltiplo de 4 deve acontecer depois de dizer se é par ou ímpar.
# - A mensagem final NÃO pode estar dentro do while.

# RESOLUÇÃO------------------------------------------------------------------------

x = 20
while x >= 0:
    print(x)
    
    if x % 2 == 0: # O operador "%" dá o resto da divisão.
        print ('x é par')
    else:
        print ('x é impar')
    if x % 4 == 0: # Se o número é divisível por 4, imprime a mensagem extra.
        print('Então x é múltiplo de 4!')
    x = x - 1 # Aqui está o motor da contagem decrescente. Sem isto, o ciclo nunca avança!
        
print('Fim da classificação!')
    
# MUITO IMPORTANTE:
#               if + if → perguntas independentes (pode acontecer mais do que uma condição)
#               if + elif + else → escolhas exclusivas, se uma é verdadeira, as outras deixam de fazer sentido)
#               else → “todos os outros casos possíveis”

    
