

ponto = 0
questao = 1

while questao <= 3: # O teste tem e questões de escolha multipla.
    resposta = input(f"Resposta da questão {questao}: ")
    
    if questao == 1 and resposta == "b": # a 'b' é a letra da resposta certa.
        ponto = ponto + 1 # ponto += 1
    if questao == 2 and resposta == "a":
        ponto += 1
    if questao == 3 and resposta == "d":
        ponto += 1
        
print(f"O aluno fez {ponto}ponto(s) no teste! ")

