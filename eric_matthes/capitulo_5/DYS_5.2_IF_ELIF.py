toppings = ['cebola', 'cogumelos', 'abacate', 'pepperoni', 'anchovas', 'ananas', 'queijo', 'tomate', 'azeitonas']

if 'jalapenhos' in toppings:
    print("Adding jalapenhos.")
elif 'cebola' in toppings:
    print("Adding cebola.")
elif 'abacate' in toppings:
    print("Adding abacate.")
elif 'anchovas' in toppings:
    print("Adding anchovas")
elif 'tomate' in toppings:
    print("Adding tomate")
print("\nDough, sauce, cheese... your pizza is officially in the making!")

# 
# O só corre nos "elif" até ao primeiro ser "TRUE" e depois pára automáticamente, SEM correr o resto do programa, os OUTROS TESTES NUNCA SÃO VERIFICADOS.