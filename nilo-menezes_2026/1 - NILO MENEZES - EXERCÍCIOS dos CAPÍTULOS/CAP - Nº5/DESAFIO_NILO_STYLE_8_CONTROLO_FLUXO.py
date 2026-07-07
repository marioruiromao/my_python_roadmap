
# Para CONTROLO DE FLUXOS:

inicio = int(input("Começar em que número? "))
incremento = int(input("Incremento? "))
limite = int(input("Limite máximo? "))

x = inicio

while x <= limite:
    print(x)
    x += incremento

# 🎯 5. A versão inteligente (que funciona para qualquer caso)=====================================================================================================

inicio = int(input("Começar em que número? "))
incremento = int(input("Incremento (pode ser negativo): "))
limite = int(input("Limite: "))

x = inicio

if incremento > 0:
    while x <= limite:
        print(x)
        x += incremento
else:
    while x >= limite:
        print(x)
        x += incremento
