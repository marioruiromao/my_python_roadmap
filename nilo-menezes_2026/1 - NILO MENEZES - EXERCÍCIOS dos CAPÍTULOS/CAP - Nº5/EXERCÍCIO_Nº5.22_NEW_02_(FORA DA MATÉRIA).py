# ------------------------------------------------------------
# EXERCÍCIO — TABUADA COM PASSO PERSONALIZADO (CAP 5)
# ------------------------------------------------------------
#
# Crie um programa que apresente o seguinte escolha:
#
# 1 - Adição
# 2 - Subtração
# 3 - Divisão
# 4 - Multiplicação
# 5 - Exit
#
# O programa deve funcionar assim:
#
# 1. O utilizador escolhe uma opção do escolha.
#
# 2. Se escolher a opção 5, o programa deve terminar.
#
# 3. Se escolher uma operação válida (1 a 4):
#       - O programa deve pedir um número base para gerar a tabuada.
#       - Depois deve pedir:
#             * O número inicial da tabuada
#             * O número final da tabuada
#             * O valor do "passo" (de quanto em quanto o contador avança)
#
# 4. O programa deve então mostrar a tabuada da operação escolhida,
#    começando no número inicial, terminando no número final,
#    e avançando de acordo com o passo escolhido.
#
# 5. O programa deve repetir o escolha até o utilizador escolher 5.
#
# Regras:
# - Não utilizar dicionários.
# - Utilizar apenas while, if/elif/else, variáveis e f-strings.
# - O passo deve ser um número inteiro positivo.


#       ============== RESOLUÇÃO ===============


while True:     # Usamos "while True" só deve ser usado quando: 1) o número de repetições é desconhecido 2) Existe um break claro dentro do loop
    print("""
             
             1 - Adição 
             2 - Subtração 
             3 - Divisão 
             4 - Multiplicação 
             5 - Exit
                 
        """)
    
    escolha = int(input("Escolha o número da operação que deseja! Para sair digite '5': "))
    
    if escolha == 5:
        break

    elif 1 <= escolha < 5:

        numero_inicial = int(input('Digite o primeiro número: '))
        numero_final = int(input('Digite o último número: '))
        contador = int(input('Digite o valor do incremento do contador: '))

        x = numero_inicial
        
        while x <= numero_final:    # Usamos "while" porque: 1) while inicio <= fim 2) E porque é um loop controlado por contagem.
            
            if escolha == 1:
                print(f"{x} + {numero_inicial} = {x + numero_inicial}")
            
            elif escolha == 2:
                print(f'{x} - {numero_inicial} = {x - numero_inicial}')
            
            elif escolha == 3:
                print(f'{x} / {numero_inicial} = {x / numero_inicial}')
            
            elif escolha == 4:
                print(f'{x} x {numero_inicial} = {x * numero_inicial}')
            
            x += contador

    else:
        print('Error!!')

    
