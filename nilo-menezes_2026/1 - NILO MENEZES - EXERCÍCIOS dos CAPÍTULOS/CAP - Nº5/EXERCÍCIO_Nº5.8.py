
#PROBLEMA: multiplicação com SOMA.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

x = 1    # Criar a variável 'x' e colocar lá o valor 1. O 'x' vai-nos dizer em que repetição do CICLO estamos.
          
r = 0    # O 'r' é a variável onde vamos guardar o RESULTADO. Começa em ZERO porque vamos fazer somas sucessivas, e ainda não fizemos nenhuma!
              
while x <= n2:
    r = r + n1    # É o coração, soma o n1 ao resultado 'r'. Repetindo isto várias vezes, e estamos a fazer multiplicação por somas sucessivas.
                              
    x = x + 1     # Esta linha faz o contador 'x' avançar uma unidade. SEM ESTE COMANDO AS REPETIÇÕES ERAM ETERNAS!!!
              
    print(f"{n1} x {n2} = {r}")    # O print está dentro do 'while', por isso só vou ver os PARCIAIS e NÃO o resultado final. Tinha que estar fora!
                                 