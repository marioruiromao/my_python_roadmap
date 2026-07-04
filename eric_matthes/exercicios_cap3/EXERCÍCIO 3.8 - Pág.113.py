metros = float(input(f"Introduza um valor em metros:"))
# NBH - Um input() devolve sempre um string, mesmo que intruduzamos um número, mesmo que tire as "aspas", o que iria dar erro pois não posso multiplicar string por números.
milímetros = metros*1000
print(f"Esta fórmula vai dizer-me que {metros}m equivalem a {milímetros:.2f}mm")
# NBH - Tenho que colocar sempre o "f" do string, caso contrário vão-me aparecer as expressões que escrevi dentro das chavetas, e não os valores que quero.
        
