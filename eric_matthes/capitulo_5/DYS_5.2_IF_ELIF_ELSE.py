
# NOTA IMPORTANTE: o "break" só pode ser usado dentro de um ciclo (while, for), nunca fora dele.
while True:
    age = int(input("Digite a sua idade para saber o preço da entrada. Para parar digite '0': "))

    if age == 0:
        print("Programa terminado. 👋")    # NBH: Se colocar o 'break' antes, o Python sai do ciclo e não executa o 'print' dentro desse ciclo.
        break       # sai do ciclo e termina o programa

    if age < 10:
        price = 15
    elif age < 18:
        price = 25
    elif age < 35:
        price = 30
    elif age < 40:
        price = 35
    elif age < 55:
        price = 28
    else:
        price = 10
    print(f"O valor que irá pagar é de {price:.2f}€. Varia com a idade!")

