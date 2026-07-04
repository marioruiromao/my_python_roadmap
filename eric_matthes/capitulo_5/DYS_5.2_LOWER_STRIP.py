nome = '                      Ana  cristINA  CoRReIa     '
nome_limpo = " ".join(nome.split()).lower()
print(nome_limpo == 'ana cristina correia')

# EXPLICAÇÃO: 

# A string original tem muitos espaços antes e depois,
# e letras com maiúsculas/minúsculas misturadas.
nome = '                      Ana  cristINA  CoRReIa     '

# strip() remove apenas os espaços do início e do fim.
# lower() transforma tudo em minúsculas.
# MAS isto não resolve os espaços a mais ENTRE as palavras.
print(nome.strip().lower() == 'ana cristina correia')   # Isto dá False

# Para limpar espaços internos, usamos split() e join():
# 1) nome.split() separa as palavras e elimina espaços extra.
#    Exemplo: ['Ana', 'cristINA', 'CoRReIa']
# 2) " ".join(...) junta as palavras com UM espaço entre cada uma.
# 3) lower() normaliza tudo para minúsculas.
nome_limpo = " ".join(nome.split()).lower()

# Agora sim, o nome fica totalmente limpo e normalizado.
print(nome_limpo == 'ana cristina correia')   # Isto dá True


# VERSÃO  PROFISSIONAL:
# A função normalizar() serve para limpar texto de forma robusta.
# Ela faz 3 coisas:
# 1) split()  → separa as palavras e remove espaços extra
# 2) " ".join → junta as palavras com UM espaço entre cada uma
# 3) lower()  → transforma tudo em minúsculas
def normalizar(texto):
    return " ".join(texto.split()).lower()


# Exemplo de uso:
nome = '                      Ana  cristINA  CoRReIa     '

# Aplicamos a função normalizar() ao nome
nome_limpo = normalizar(nome)

# Mostramos o resultado
print(nome_limpo)  # deve mostrar: ana cristina correia

# Teste robusto
print(nome_limpo == 'ana cristina correia')  # True
