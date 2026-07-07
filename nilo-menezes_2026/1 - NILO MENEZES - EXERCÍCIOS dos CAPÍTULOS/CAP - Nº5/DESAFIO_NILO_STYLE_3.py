# DESAFIO: Classificação de Temperaturas
#
# Objetivo:
# Criar um programa que usa um ciclo while e condições if/elif/else.
#
# Enunciado:
# 1. O programa deve começar com o valor 30.
# 2. Deve fazer uma contagem decrescente até 0.
# 3. Para cada número (que representa uma temperatura em graus Celsius):
#       - Se a temperatura for maior ou igual a 25, imprimir: "Muito quente"
#       - Se estiver entre 15 e 24, imprimir: "Agradável"
#       - Se estiver entre 5 e 14, imprimir: "Fresco"
#       - Se estiver entre 1 e 4, imprimir: "Frio"
#       - Se for 0, imprimir: "Congelado!"
# 4. No fim da contagem, imprimir apenas uma vez: "Fim da análise!"
#
# Notas:
# - Usa if, elif e else para criar as faixas de temperatura.
# - A ordem das condições é importante.
# - O print final NÃO pode estar dentro do while.

# SOLUÇÃO:--------------------------------------------------------------

x = 30                        

while x >= 0:                   
    print(x)                    
# Agora classificamos o próprio x que acabámos de imprimir:
    if x < 4:                   # Primeiro, o caso mais frio (intervalo mais restrito).
        print('Frio')
    elif x < 15:                # Se não for < 4, mas for < 15...
        print('Fresco')
    elif x < 25:                # Se não for < 15, mas for < 25...
        print('Agradável')
    elif x < 30:                # Se não for < 25, mas for < 30...
        print('Muito quente')
    else:                       # Se não caiu em nenhum dos anteriores, é porque é >= 30.
        print('Escaldante!')    

    x = x - 1                   # No fim da iteração, fazemos a contagem decrescente.

print('Fim da análise!')        # Quando x ficar < 0, saímos do while e imprimimos isto.

# Regra de ouro para memorizar:-------------------------------------------
# 1 - A posição da atualização só importa quando existe repetição;
# 2 - Se não há ciclo (while), não há atualização obrigatória.
# ------------------------------------------------------------------------