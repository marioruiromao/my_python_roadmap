
salario = float(input(f"Diz-me o salário:"))
aumento = float(input(f"Percentagem do aumento:"))
# Mas não há nenhuma expressão {} dentro da string. Logo, o f é desnecessário.
# Fica mais limpo assim: aumento = float(input("Percentagem do aumento:"))

aumento_percentual = aumento/100
# salario_final = salario * (1 + percentagem / 100) Assim evito a linha anterior
salario_final = salario + salario * aumento_percentual

print(f"Sálário com o aumento dá {salario_final:.2f}")
