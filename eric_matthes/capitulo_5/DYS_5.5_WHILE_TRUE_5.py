# ENUNCIADO

# Escreva um programa que leia repetidamente uma idade.
# O programa deve parar apenas quando o utilizador digitar 999.

# A idade deve ser validada: só são aceites valores entre 0 e 120 anos.
# Enquanto a idade estiver fora deste intervalo, o programa deve pedir um novo valor.

# Depois de validada, a idade deve ser classificada da seguinte forma:

# 0 a 12      → "Criança"
# 13 a 17     → "Adolescente"
# 18 a 64     → "Adulto"
# 65 a 120    → "Idoso"

# Não usar listas, nem funções, nem estruturas avançadas.
# Usar apenas: while True, while de validação, if/elif/else e break.

while True:
    print("Vamos classificar idades entre os 0 e os 120 anos. ")

    idade = int(input("Digite uma idade! Para parar coloque 999: "))

    if idade == 999:
        print("Sair do programa.")
        break

    while idade < 0 or idade > 120: 
        print("Erro! A idade digitada está fora do intervalo definido. Digite uma outra! ")
        idade = int(input("Digite uma idade, mas tem que ser entre os 0 e os 120 anos"))
    
    if idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 64:
        print("Adulto")
    else:
        print("Idoso")  # Não temos "alucinações lógicas" aqui como o Eric M. diz, porque o "while" 
                        # define um intervalo, não aceitando nada fora dele.


