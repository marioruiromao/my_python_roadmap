#falta colocar os segundos e tirar as letras antes de aplicar as fórmula. Isto é só para me orientar na minha linha de raciocínio.

#segundos_por_dias = (d) * 24 * 60 * 60
#segundos_por_horas = (h) * 60 * 60
#segundos_por_minutos = (m) * 60

#Deviamos escrever em letra maiúsculas, para destacar:

segundos_por_dias = 24 * 60 * 60
segundos_por_horas = 60 * 60
segundos_por_minutos = 60


#se tivesse colocado "int" estava ótimo também.

#SUPER IMPORTANTE - o "input" SÓ ACEITA TEXTO, pois devolve sempre uma "string"
#  input() devolve sempre uma string → "3", "4.5", "0".
#  float(...) converte essa string para número decimal → 3.0, 4.5, 0.0.
#  Sem o float(), ficarias com texto, e não poderias fazer contas.

dias = float(input("Diga os dias:"))
horas = float(input("Diga as hora:"))
minutos = float(input("Diga os minutos:"))
segundos = float(input("Diga os segundos:"))

total_segundos = (
    
    dias * segundos_por_dias
    + horas * segundos_por_horas
    + minutos * segundos_por_minutos
    + segundos
    
    )

# Sim, Mário — as chavetas { } dentro de uma f‑string significam exatamente isso: o Python vai buscar o valor atual da variável e colocá‑lo ali, já formatado.
# Ou seja: as chavetas não são texto — são um marcador que o Python substitui pelo valor real da variável naquele momento.

print(f"Dá-nos um total de {total_segundos:.2f}segundos")
