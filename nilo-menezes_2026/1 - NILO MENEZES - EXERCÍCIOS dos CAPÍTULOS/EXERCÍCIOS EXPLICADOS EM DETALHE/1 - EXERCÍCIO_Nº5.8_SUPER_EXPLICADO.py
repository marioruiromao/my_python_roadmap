
#PROBLEMA: multiplicação com SOMA.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

x = 1 # Cria a variável 'x' e coloca lá o valor 1.  O 'x' vai-nos dizer em que repetição do CICLO estamos.
      # O 'x' é uma variável que nos vai servir como CONTADOR dentro do ciclo while.
      # Como 'x' começa em 1 e a condição é x <= n2, o ciclo vai repetir exatamente n2 vezes
    
r = 0  # O 'r' é a variável onde vamos guardar o RESULTADO. Começa em ZERO porque vamos fazer somas sucessivas, e ainda não fizemos nenhuma.
       # Quando somamos coisas, o ponto de partida natural é ZERO. Se ainda não somamos nada, temos ZERO, resultados.
       # o 'r' é um ACUMULADOR: começa em 0 e vai guardando o resultado parcial a cada repetição.
       
while x <= n2:
    r = r + n1 # É o coração, soma o n1 ao resultado 'r'. Repetindo isto várias vezes, e estamos a fazer multiplicação por somas sucessivas.
               # Depois de n2 repetições, r é igual a n1 somado n2 vezes, ou seja, n1 * n2.
               
    x = x + 1 # Esta linha faz o CONTADOR 'x' avançar uma unidade. SEM ESTE COMANDO AS REPETIÇÕES ERAM ETERNAS!!!
              # Ao aumentar 'x', aproximamo-nos do momento em que 'x' deixa de ser <= n2 e o ciclo termina.

    print(f"{n1} x {n2} = {r}")   # O print está dentro do 'while', por isso só vou ver os PARCIAIS e NÃO o resultado final.
                                  # Para mostrar apenas o RESULTADO FINAL, o print deve ficar FORA do while.



# NT: o  RESULTADO ( r ) na SOMA é sempre ZERO (r = 0) e na MULTIPLICAÇÃO é UM (r = 1)
