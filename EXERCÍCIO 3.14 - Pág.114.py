
quantidade_km = float(input("Kms percorridos: "))
# os dias à partida são inteiros por isso posso usar números inteiros (%d)
quantidade_dias = int(input("Dias alugado: "))

preço_carro = quantidade_km * 0.15 + quantidade_dias * 60

#O 8.2f reserva pelo menos 8 caracteres, com 2 casas decimais.
print(f"Preço final do carro: {preço_carro:8.2f} €")


#  ----VERSÃO PYTHONIC----

quantidade_km = float(input("Quilómetros percorridos: "))
quantidade_dias = int(input("Número de dias de aluguer: "))

PRECO_POR_DIA = 60
PRECO_POR_KM = 0.15

preco_total = quantidade_km * PRECO_POR_KM + quantidade_dias * PRECO_POR_DIA

print(f"Preço total do aluguer: {preco_total:7.2f} €")
