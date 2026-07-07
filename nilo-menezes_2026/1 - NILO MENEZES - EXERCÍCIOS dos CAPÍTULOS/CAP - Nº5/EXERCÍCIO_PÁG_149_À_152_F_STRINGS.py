a = 'Mário & Python'
print(f'Como estão {a}?')

# criar espaçamentos

preco = 5.20
print(f"Preço:{preco:5.2f}€")

preco = 510.99
print(f'Preço:€{preco:15.2f}')

preco = 510.99
print(f'Preço:€{preco:.2f}')

# Alinhar valores à esquerda'>', direita'<' ou ao centro'^'

preco = 510.99
print(f'Preço:€{preco:15.2f}')

preco = 510.99
print(f'Preço:€{preco:>15.2f}') # à DIREIRA

preco = 510.99
print(f'Preço:€{preco:<15.2f}') # à ESQUERDA

preco = 510.99
print(f'Preço:€{preco:^15.2f}') # ao CENTRO

# Podemos ainda definir um caracter para preencher o vazio, se assim quisermos!

preco = 510.99
print(f'Preço:€{preco:_^15.2f}')

preco = 510.99
print(f'Preço:€{preco:*<15.2f}')

preco = 510.99
print(f'Preço:€{preco:->15.2f}')

# Usar funções dentro de f-string

x = 5.1
print(f"Inteiro: {int(x)}")

# Operações MATEMÁTICAS:

preco = 1.26
print(f"O preço atualizado é:{preco * 10:_^15.3f}€")

# Multiplas linhas: ASPAS TRIPLAS PREFIXADAS COM 'f'

print(f"""
      O encontro foi um sucesso!
      Na próxima vez vamos tentar juntar mais pessoas!
      """ )

# Mas podemos usar em vez disso: \n

print(f"""\nO encontro foi um sucesso! \nNa próxima vez vamos tentar juntar mais pessoas! \nIsto tem sido incrivel! \nSó mesmo visto, para acreditar.""" )

# Usar ("") ou ('') triplas, e dentro simples.

print("""Assim eu consigo destacar 'palavras' sem qualquer problema, será?""")

print('''Afinal é "possivel" fazer isso''')

# Também é possivel uar aspas dentro de outras com ( \ ) sem ter que usar aspas triplas:

print("Afinal há vária hipóteses para usar \"aspas\"! É só uma questão de estudar e ver o que é \"possível\" fazer. É \"absolutamente\" incrível.")