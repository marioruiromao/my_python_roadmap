
# SUPER NOTA:
# O 'while' é como uma porta que só fecha quando a condição deixa de ser verdadeira.
# Enquanto a condição for verdadeira → o código lá dentro continua a repetir.
# Quando a condição deixar de ser verdadeira → o ciclo pára. 
# ==================================================================================

x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")


# NOVO PROBLEMA:

ultimo = int(input('Digite o último número à sua escolha: '))

if ultimo < 1: # Isto serve para dar mensagem de erro!
    print('Erro! Valor inválido')
else:      # NBH: O else corre SEMPRE que o while não entra, ou termina, por isso tem que ficar antes, isto é: no caso de querermos usar 'mensagens de erro'!
    x = 1
    while x <= ultimo:
        print(x)
        x += 2 # Para ir de um número ímpar para o próximo número ímpar somamos 2.

    


    
