
preço_mercadoria = float(input("Preço da mercadoria(€): "))
percentagem_desconto = float(input("Desconto(%):"))

valor_desconto = preço_mercadoria*percentagem_desconto/100
valor_a_pagar = preço_mercadoria - valor_desconto

print(f"Desconto:{valor_desconto:.2f} €")
print(f"O preço final: {valor_a_pagar:.2f} €")
