while True:  
    
    print("""
    Menu

    1 - Adição
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    5 - Exit
    """)  

    escolher = int(input("Escolha o número do menu que quer: "))
  
    if escolher == 5:
        break  

    elif 1 <= escolher < 5:     # Em vez de escrever ">=1 and <5", uso uma condição mais limpa e Pythonic.

        n = int(input("Escolha a tabuada de: "))

        x = 1  # Inicio o contador da tabuada.

        while x <= 10:       # Loop para gerar a tabuada até 10.

            if escolher == 1:
                print(f"{n} + {x} = {n + x}")  # Adição

            elif escolher == 2:
                print(f"{n} - {x} = {n - x}")  # Subtração

            elif escolher == 3:
                print(f"{n} / {x} = {n / x}")  # Divisão

            elif escolher == 4:
                print(f"{n} x {x} = {n * x}")  # Multiplicação

            x += 1  # Incremento do contador.

    else:
        print("Erro: opção inválida!")      # Aqui trato opções fora do intervalo permitido.

    # VERSÃO MAIS PYTHONIC ==================================================================

    operacoes = {1: "+", 2: "-", 3: "/", 4: "*"}

while True:
    print("""
    Menu

    1 - Adição
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    5 - Exit
    """)

    escolher = int(input("Escolha o número do menu que quer: "))

    if escolher == 5:
        break

    elif 1 <= escolher <= 4:
        n = int(input("Escolha a tabuada de: "))
        x = 1

        while x <= 10:
            op = operacoes[escolher]  # Busco o símbolo da operação no dicionário

            if op == "+":
                resultado = n + x
            elif op == "-":
                resultado = n - x
            elif op == "/":
                resultado = n / x
            elif op == "*":
                resultado = n * x

            print(f"{n} {op} {x} = {resultado}")
            x += 1

    else:
        print("Erro: opção inválida!")






