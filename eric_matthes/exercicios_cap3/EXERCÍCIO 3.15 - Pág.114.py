# Constante (em maiúsculas, como manda a convenção)
MINUTOS_DIA = 1440

cigarros_por_dia = int(input("Quantos cigarros fuma por dia: "))
anos_de_fumo = int(input("Há quantos anos fuma: "))


total_cigarros_fumados = cigarros_por_dia * (anos_de_fumo * 365)


dias_vida_perdida_fumantes = total_cigarros_fumados * 10 / MINUTOS_DIA
#SUPER DICA: este tipo de diviões gera normalmente nº decimais e NÃO INTEIROS!!
input(f"Dias de vida perdidos: {dias_vida_perdida_fumantes:.2f}")


# --- SUPER DICAS ---

# 1. Captura e Armazenamento
nome = input("Digite seu nome: ")
# 2. Processamento ou Saída (usando f-string, que é o padrão moderno)
print(f"Olá, {nome}! É um prazer te conhecer.")

# --- SUPER DICAS ---

#Não podes usar precisão (.2) num formato de inteiro (d).Portanto, o erro está no .2d.
#Se queres mostrar o número como inteiro normal:
#python
#print(f"Total de cigarros fumados: {total_cigarros_fumados:d}")
#Ousimplesmente:
#python
#print(f"Total de cigarros fumados: {total_cigarros_fumados}")
#Se queres mostrar com zeros à esquerda (ex.: 02, 003, 0005). Usa largura, não precisão:
#python
#print(f"Total de cigarros fumados: {total_cigarros_fumados:02d}")
#Aqui:
#0 → preenche com zeros
#2 → largura mínima de 2 caracteres
#d → inteiro
