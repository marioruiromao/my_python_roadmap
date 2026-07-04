valor_em_metros = float(input(f"Escreva um valor em metros:"))
valor_em_milimetros = valor_em_metros * 1000
print(f"O seu valor {valor_em_metros}m equivale a {valor_em_milimetros:.4f}em milímetros")
                                
# versão mais elegante e Pythonica!

metros = float(input("Valor em metros: "))
mm = metros * 1000
print(f"{metros:.2f} m = {mm:.0f} mm")
