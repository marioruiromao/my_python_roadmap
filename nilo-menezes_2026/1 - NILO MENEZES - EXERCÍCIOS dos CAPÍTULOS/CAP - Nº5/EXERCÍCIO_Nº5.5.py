
# PROBL - Resscrever o problema para imprimir apenas os 10 primeiros múltiplos de 3.


ultimo_nº = 30 # Como cheguei a este valor? Quais são os 10 primeiros múltiplos de 3?
               # 1º múltiplo: 3*1=3, 3*2=6...último multiplo 3*10=30. *Passamosa saber o 1º e o último.

x = 3

while x <= ultimo_nº:
    print(x) # print(x) vem antes de( x += 2 ), e evita imprimir valores acima do limite.
    x += 3
