#  EXERCÍCIO 5.23

# SUPER DICA: 1ª) Começar sempre primeiro por tratar os casos especiais, 2º) depois o caso geral.

quantidade = int(input("Quantos números primos deseja gerar? "))

if quantidade <= 0:         # Caso particular
    print("Erro! Digite um valor positivo.")
else:           
    print(2)                # Primeiro primo conhecido
    numeros_a_gerar = 1     # É um "contador" começa em 1, e não em "0", porque já tinha imprimido o "2".
    numero = 3              # começamos a testar a partir de 3

    while numeros_a_gerar < quantidade:

        divisor = 3
        # Testa apenas divisores ímpares
        while divisor < numero:
            if numero % divisor == 0:   # LÊ-SE: O resto da divisão dO "numero" pelo "divisor" é igual a zero.
                break
            divisor = divisor + 2

        # Se não encontrou divisor → é primo
        if divisor == numero:
            print(numero)
            numeros_a_gerar = numeros_a_gerar + 1

        # passa para o próximo ímpar
        numero = numero + 2


