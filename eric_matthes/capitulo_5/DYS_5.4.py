print(

    'green',
    "   "
    'yellow',
    "   "
    'red'

    )

allien_color = input("Escolha uma das três cores da lista: ").strip().lower()

if allien_color != 'green' and allien_color != 'yellow' and allien_color != 'red':
    print("Oops, wrong color! Pick the correct one.")

elif allien_color == 'green':
    print("You got 50 stars just for blasting an alien")

else:
    print("You racked up 8000 stars")


# NOTAS IMPORTANTES:

# .strip() - Remove espaços em branco (e caracteres de nova linha \n, \t) do início e do fim da string.
#        .lstrip() → remove SÓ à esquerda
#        .rstrip() → remove SÓ à direita
#        .strip("x") → remove o caractere "x" das extremidades
#        \n — Nova Linha (newline), move o cursor para a linha seguinte.
#        \t — Tabulação (tab), insere um espaço horizontal equivalente a uma tabulação (normalmente 4 ou 8 espaços).

# .lower() - Converte todos os caracteres para minúsculas.
