
distancia_a_percorrer = float(input(f"Distância a percorrer(km): "))
velocidade_media = float(input(f"Velocidade média (Km/h): "))

tempo_medio_viagem = distancia_a_percorrer / velocidade_media
Conversão_minutos = tempo_medio_viagem * 60

print(f"O tempo de viagem será {tempo_medio_viagem:.2f} h")
print(f"O tempo médio em minutos foi: {Conversão_minutos:.2f} min")

#Como se faz a conversão?
# A regra é simples: minutos = horas * 60


#VERSAO PYTHONIC:

distancia_km = float(input("Distância a percorrer (km): "))
velocidade_kmh = float(input("Velocidade média (km/h): "))

tempo_horas = distancia_km / velocidade_kmh
tempo_minutos = tempo_horas * 60

print(f"Tempo de viagem: {tempo_horas:.2f} h")
print(f"Tempo de viagem: {tempo_minutos:.2f} min")
