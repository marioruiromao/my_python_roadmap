
MINUTOS_DIA = 1440  # constante (maiúsculas = convenção Python)

cigarros_por_dia = int(input("Quantos cigarros fuma por dia: "))
anos_de_fumo = int(input("Há quantos anos fuma: "))

total_cigarros_fumados = cigarros_por_dia * (anos_de_fumo * 365)
print(f"Total de cigarros fumados: {total_cigarros_fumados}")

dias_vida_perdida_fumantes = total_cigarros_fumados * 10 / MINUTOS_DIA
print(f"Dias de vida perdidos: {dias_vida_perdida_fumantes:.2f}")

#Nota 1 — Constantes em maiúsculas

#Correção:
#Em Python, valores que não devem mudar ao longo do programa são escritos em MAIÚSCULAS.
#Isto não é obrigatório, mas é uma convenção universal para melhorar a leitura do código.
#Fundamentação: ajuda outros programadores a perceber que aquela variável é “fixa”. Segue o PEP 8, o guia oficial de estilo do Python.

# --- SUPER DICA ---
#Nota 2 — Nunca usar input() dentro de print()
#Correção:
#input() serve para ler dados.
#print() serve para mostrar dados.
#Misturar os dois causa comportamentos inesperados e obriga o utilizador a carregar ENTER extra.

#Fundamentação: input() pausa o programa até o utilizador escrever algo.
#Se estiver dentro de print(), o programa pausa DUAS vezes. Isto quebra o fluxo e impede o programa de correr até ao fim.

# Nota 3 — SUPER DICA: as divisões com / geram floats
#A tua nota estava quase certa, mas vamos afiná‑la:
#Correção: em Python, a operação / devolve sempre um número do tipo float, mesmo que a divisão seja exata.
#Fundamentação:
#10 / 5 → 2.0 (float)
#7 / 2 → 3.5 (float)
#Isto é comportamento padrão do Python desde a versão 3.0.
#Consequência prática: Não podes formatar o resultado com :d (inteiro). Tens de usar .2f, .1f, etc.

#Nota 4 — Formatação correta
#Correção:
#Usa :d apenas para inteiros.
#Usa .2f para floats com duas casas decimais.
#Fundamentação:
#:d = decimal integer
#.2f = float com 2 casas decimais

#Misturar os dois gera erros como: ValueError: Unknown format code 'd' for object of type 'float'
