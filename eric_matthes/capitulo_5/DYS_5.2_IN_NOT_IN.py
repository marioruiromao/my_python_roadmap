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
print("Is pessego in fruta? I do not think so! False")
print('pessego'in fruta)


print("Is banana in fruta? I think so! - True")
print('banana' in fruta)


print("Is macarrao not in fruta? Yes - True")
print('macarrao' not in fruta)

print("Is banana in fruta or bolo in fruta? Yes - True")
print('banana' in fruta or 'bolo' in fruta)

print("is cogumelo not in fruta and baleia not in fruta? True")
print('cogumelo' not in fruta and 'baleia' not in fruta)