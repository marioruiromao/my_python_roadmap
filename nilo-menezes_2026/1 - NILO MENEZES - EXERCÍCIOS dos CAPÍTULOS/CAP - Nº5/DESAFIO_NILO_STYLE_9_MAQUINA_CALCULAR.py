
#EXERCICIO: uma máquina de cálcular, em que eu possa definir:

#           1 - O número da tabuada que quero;
#           2 - O incio da contagem;
#           3 - O fim da contagem;
#           4 - No formato tipíco da tabuada.
#           5 -Não esquecer embelezar com ASCII

# RESOLUÇÃO:

tabuada = float(input('Digite a tabuada que quer: '))
incio = float(input('Digite o primeiro número da tabuada: '))
fim = float(input('Digite o último número da tabuáda: '))

titulo = f"TABUADA DO {tabuada:.2f}".strip() # O strip() vai: remover espaços antes e depois, garantir que o título tem exatamente o tamanho certo e evitar desalinhamentos
largura = len(titulo) + 4 # 2 espaços e + 2 barras laterais

linha = "+" + "-" * (largura - 2) + "+"

print(linha)
print(f"| {titulo} |")
print(linha)


print('\n') # imprime 2 linhas vazias. print(): imprime 1 linha vazia. print('\n\n'): 3 linhas. 
            # E para imprimir texto seria: print("\n=== TABUADA ===\n")


x = incio

while x <= fim:
    
    produto = tabuada * x
    
    print(f"{tabuada:.2f} * {x:.2f} = {produto:.2f}")
    
    x += 1 # SEM esta expressão o cicclo era infinito!


    
#========================================================================================
# SUPER IMPORTANTE:

# Pensa assim: 'inicio' e 'fim são como marcas fixas numa régua.
# O 'x' é o dedo que se move da marca 'inicio' até à marca 'fim'.
# As marcas não mudam, o que muda é o dedo é que se mexe.
#=========================================================================================
