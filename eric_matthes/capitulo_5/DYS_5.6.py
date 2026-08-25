# PROBLEMA: Fases da Vida
print("Digite idades para ver a fase da vida. Para parar, digite 777.\n")

while True:
    idade = float(input("Idade: "))

    if idade == 777:
        print("\nPrograma encerrado!")
        break

    if idade < 0 or idade > 120:
        print("Idade inválida. Tente novamente.\n")
        continue

    if idade <= 2:
        print("Bebé\n")
    elif idade <= 4:
        print("Criança\n")
    elif idade <= 13:
        print("Pré-adolescente\n") # com o '\n' no fim, significa que vai ficar um espaço em baixo. Se fosse antes, era um espaço em cima!
    elif idade <= 20:
        print("Adolescente\n")
    elif idade <= 65:
        print("Adulto\n")
    else:
        print("Idoso\n")





