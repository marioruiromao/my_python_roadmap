# Criar uma lista com as cores permitidas
cores = ['green', 'yellow', 'red']

# Para mostrar as cores ao utilizador
print("Cores disponíveis:", cores)

# Aqui estou a pedir a cor e a normalizar
alien_color = input("Escolhe uma cor: ").strip().lower()

# Aqui estou a verificar se a cor está na lista
if alien_color not in cores:
    print("Cor inválida. Tens de escolher uma das cores da lista.")
elif alien_color == 'green':
    print("You got 500 stars just for blasting an alien")
else:
    print("You racked up 8000 stars")
