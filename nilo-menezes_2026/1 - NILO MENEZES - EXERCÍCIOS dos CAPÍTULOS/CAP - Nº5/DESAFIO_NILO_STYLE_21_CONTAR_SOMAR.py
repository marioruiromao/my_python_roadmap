
# EXERCÍCIO: Nível 1 — Contar e Somar Separadamente

# Lê vários números inteiros do utilizador.
# O programa termina quando o utilizador digitar -1.
#
# Durante a leitura:
#   - Conta quantos números foram digitados (CONTADOR)
#   - Soma todos os números digitados (ACUMULADOR)
#
# No final, mostra:
#   - Quantidade total de números
#   - Soma total dos números



# RESOLUÇÃO:

contador = 0        # É o nosso contador!
soma = 0            # É o nosso acumulador!

while True:
    numeros_inteiros = int(input('Digite vários números inteiros! Quando quiser parar digite "-1": ' )) 
    if numeros_inteiros == -1:
        break

    contador += 1                   # CONTADOR: aumenta 1 porque o utilizador digitou um número válido.
    soma += numeros_inteiros        # ACUMULADOR: somo o VALOR digitado ao total. Aqui é importante: somo o número REAL, não o contador.

print(f'Números digitados: {contador} ')
print(f'Soma dos números digitados: {soma}')


