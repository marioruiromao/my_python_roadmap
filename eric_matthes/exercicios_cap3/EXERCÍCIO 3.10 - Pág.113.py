
salario = float(input("Salário atual:"))
aumento = float(input("Percentagem de aumento:"))
novo_salario = salario * (1 + aumento / 100)

#---MUITO IMPORTANTE---:
#print(...) não devolve o valor impresso, devolve None.
#Ou seja, depois desta linha, novo_salario fica com o valor None, não com o valor do salário.
#Estavas a misturar lógica de cálculo com lógica de apresentação, quando fizeste
#isto:      novo_salario = print(f"O novo salário é de {novo_salario:.2f}€")
#O print fica sempre sozinho!

# Estas duas linhas abaixo é para caso eu queira que o simbolo do € e da € aparecem no fim dos valores. 
print(f"Salário atual: {salario:.2f}€")
print(f"Percentagem de aumento: {aumento:.2f}%")

print(f"O novo salário é de {novo_salario:.2f}€")

#NUNCA, NUNCA ESQUECER-ME: O print() mostra um VALOR mas NÃO devolve esse para ser GUARDADO numa variável. Ele fica
#com o valo None (fica sem nada)
