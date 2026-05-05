d = float(input("Diz-me dias:"))
h = float(input("diz-me horas"))
m = float(input("Diz-me minutos:"))
s = float(input("Diz-me segundos:"))
total_s = (d*24*60*60) + (h*60*60) + (m*60) + (s)
print(f"O teu total deu {total_s:.4f}segundos")



# ------------- Uma versão mais Pythonic: "ANALISAR BEM" ----------------

SEGUNDOS_POR_DIA = 24 * 60 * 60
SEGUNDOS_POR_HORA = 60 * 60
SEGUNDOS_POR_MINUTO = 60

dias = float(input("Dias: "))
horas = float(input("Horas: "))
minutos = float(input("Minutos: "))
segundos = float(input("Segundos: "))

total_segundos = (
    dias * SEGUNDOS_POR_DIA
    + horas * SEGUNDOS_POR_HORA
    + minutos * SEGUNDOS_POR_MINUTO
    + segundos
)

print(f"Total: {total_segundos:.4f} segundos"

# Porquê: em vez de “números mágicos” como 24*60*60 espalhados, dás‑lhes um nome.
#Pythonic: melhora a legibilidade e segue a ideia de “readability counts” (PEP 8).
#Maiúsculas: em Python, nomes em maiúsculas indicam “constantes” (valores que não mudam)
#Porquê: d funciona, mas obriga o cérebro a lembrar “d = dias?”. Com dias, lês o código quase como português.
#Pythonic: nomes curtos mas claros são preferidos a abreviações crípticas.
#Parênteses + quebras de linha: isto é muito Pythonic—usa a “implicit line joining” dentro de parênteses, sem \.
#Sem parênteses desnecessários em cada termo: a precedência de * e + já é clara, mas aqui a legibilidade vem da estrutura vertical.
#Nome da variável: total_segundos é mais expressivo que total_s.
#Espaço antes de “segundos”: evita 123.0000segundos.
#Texto mais curto e direto: bom estilo em programas de linha de comando.
#Manténs o :.4f: ótimo, já estás a usar formatação numérica de forma correta.

#Uma versão ainda mais estruturada (com função)
#Só para te mostrar o próximo passo “Pythonic”:

SEGUNDOS_POR_DIA = 24 * 60 * 60
SEGUNDOS_POR_HORA = 60 * 60
SEGUNDOS_POR_MINUTO = 60


def para_segundos(dias, horas, minutos, segundos):
    return (
        dias * SEGUNDOS_POR_DIA
        + horas * SEGUNDOS_POR_HORA
        + minutos * SEGUNDOS_POR_MINUTO
        + segundos
    )

dias = float(input("Dias: "))
horas = float(input("Horas: "))
minutos = float(input("Minutos: "))
segundos = float(input("Segundos: "))

total_segundos = para_segundos(dias, horas, minutos, segundos)
print(f"Total: {total_segundos:.4f} segundos")

#Função separada: o cálculo fica reutilizável e testável.
#Fluxo principal mais limpo: “ler → calcular → mostrar”.
