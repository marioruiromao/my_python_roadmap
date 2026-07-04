# Contadores principais
total_temperaturas = 0
muito_frio = 0
muito_quente = 0

while True:
    print("Vamos classificar as suas temperaturas. Para interromper, digite: '999' ")

    # --- BLOCO TRY/EXCEPT PARA EVITAR ERROS COM CARACTERES INVÁLIDOS ---
    #     O "try/except" é o guarda-costas do teu programa. Ele impede que o programa morra ANTES da validação.
    while True:
        try:
            temperatura = int(input("Introduza as temperaturas em graus Celsius: "))
            break   # Se for número válido, sai deste while
        except:
            print("Erro! Introduza apenas números inteiros. Tente novamente.")

    # Sentinela para parar o programa
    if temperatura == 999:
        print("Contagem interrompida!")
        break

    # Validação do intervalo permitido
    while temperatura < -30 or temperatura > 50:
        print("Erro! Temperatura fora dos parâmetros (-30 a 50).")
        try:
            temperatura = int(input("Introduza uma temperatura válida: "))
        except:
            print("Erro! Introduza apenas números inteiros.")
            continue  # Volta ao início da validação

    # Contador principal (só conta temperaturas válidas)
    total_temperaturas += 1

    # Classificação + contadores específicos
    if temperatura <= 0:
        print("Muito frio!")
        muito_frio += 1

    elif temperatura <= 15:
        print("Frio!")

    elif temperatura <= 25:
        print("Agradável!")

    elif temperatura <= 35:
        print("Quente!")

    else:
        print("Muito quente!")
        muito_quente += 1

# Estatísticas finais
print("\nEstatísticas finais das temperaturas registadas:")
print(f"Total de temperaturas introduzidas: {total_temperaturas}")
print(f"Temperaturas 'muito frias': {muito_frio}")
print(f"Temperaturas 'muito quentes': {muito_quente}")
