beatriz = 'filha'
leonor = 'filha'
print("Is beatriz == 'filha' and leonor == 'filha'? I predict is True")
print(beatriz == 'filha' and leonor == 'filha')


leonor = 'filha'
sebastiao = 'filho' 
print("Is leonor == 'filha' or sebastiao == 'filho'? I predect is True")
print(leonor == 'filha' or sebastiao == 'filho')


leonor = 'filha'
banana = 'fruto'
print("Is leonor == 'filha' end banana == 'filho'. I predect is False")
print(leonor == 'filha' and banana == 'filho')

idade_leonor = 16
idade_beatriz = 19
print("is idade_leonor == 16 >= idade_beatriz == 19. I predict is False")
print(idade_leonor == 16 >= idade_beatriz >= 19)

idade_beatriz = 19
idade_leonor = 16
idade_vasco = 20
idade_sebastiao = 17
print("Is idade_beatriz == 19 <= idade_sebastiao == 17. I predect is False")
print(idade_beatriz == 19 <= idade_sebastiao == 17)      # Tenho que usar '==' porque estou a fazer uma COMPARAÇÃ0!

idade_beatriz = 19          # Dentro de um teste, só podes usar operadores lógicos: ==, !=, <, >, <=, >=.
idade_leonor = 16
idade_vasco = 20
idade_sebastiao = 17
print("is idade_beatriz != 25. I think so - True")
print(idade_beatriz != 25)

idade_leonor = 16
idade_vasco = 20
print("Is idade_leonor != 18 and idade_vasco <= 30. I think so - True")
print(idade_leonor != 18 and idade_vasco <= 30)

nome = 'leonor'
surname = 'ROMAO'
print("Is surname == romao? I think so - True")
print(surname.lower() == 'romao')


idade_beatriz = 19          # SUPER DICA: Dentro de um teste, só posso usar operadores lógicos: ==, !=, <, >, <=, >=.
idade_leonor = 16
idade_vasco = 20
idade_sebastiao = 17
print("É a idade_beatriz > 20 or idade_vasco >= 100. Eu não acredito - False")
print(idade_beatriz > 20 or idade_vasco >=100)

# LISTAS 

fruta = ['banana', 'kiwi', 'ananas', 'goiaba', 'pera']

print("Is print(fruta[2]) == ananas? I predect - True")
print(fruta[2] == 'ananas')

print("is fruta[0] == banana and fruta[-3] == ananas? True")
print(fruta[0] == 'banana' and fruta[-3] == 'ananas')

print("Is fruta[-1] == 'goiaba' or fruta[0] == 'pera'? False")
print(fruta[-1] == 'goiaba' or fruta[0] == 'pera?')

fruta = ['banana', 'kiwi', 'ananas', 'goiaba', 'pera', 'manga', 'laranja', 'tomate', 'abacate']
fruta.sort()   # Ordena A → Z
print(fruta)

fruta.sort(reverse=True) # Ordena Z → A
print(fruta)


fruta = ['banana', 'kiwi', 'ananas', 'goiaba', 'pera']

print('pessego'in fruta)
