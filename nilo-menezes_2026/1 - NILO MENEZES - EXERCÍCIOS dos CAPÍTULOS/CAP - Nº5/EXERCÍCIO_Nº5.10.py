# NOTA - Não posso usar .upper ) e l.lower() ao mesmo tempo!

ponto = 0
questão = 1

while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ').strip().lower()
    if questão == 1 and resposta == 'b':
        ponto += 1
    if questão == 2 and resposta == 'a':
        ponto += 1
    if questão == 3 and resposta == 'd':
        ponto += 1
    questão += 1
print(f'O aluno fez no total {ponto} pontos')

#=======================================================================
# RESOLUÇÃO DO NILO MENEZES
#=======================================================================

pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questão += 1
print(f"O aluno fez {pontos} ponto(s)")
