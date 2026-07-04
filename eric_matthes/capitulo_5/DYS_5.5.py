# Lista de cores válidas
arco_iris = ['green', 'red', 'yellow']

print("As cores disponíveis são:", arco_iris)

# Normalizo o input para evitar erros de maiúsculas/espaços
cor = input("Escolha uma cor: ").strip().lower()

# Primeiro: validação
if cor not in arco_iris:
    print("Atenção! Essa cor não existe na lista.")
else:
    # Depois: lógica do jogo
    if cor == 'green':
        print("You got 10 points and can blow up an alien")
    elif cor == 'yellow':
        print("You earned 500 points and now you can blast an alien")
    elif cor == 'red':
        print("You scored 8000 points and can take out an alien")

