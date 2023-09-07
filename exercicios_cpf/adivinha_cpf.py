#Cálculo do primeiro dígito do CPF
cpf = input('Digite os nove primeiros dígitos do seu CPF: ')
cpf9 = ''
for digito in cpf:
    if len(cpf9) == 9:
        break
    if digito.isdigit() == False:
        continue
    else:
        cpf9 += digito
regressiva = 10
soma = 0
for numero in cpf9:
    mult = int(numero) * regressiva
    soma += mult
    regressiva -= 1

mult2 = soma * 10
digito1 = mult2 % 11
primeiro_digito = digito1 if digito1 <= 9 else 0 
print(f'O primeiro dígito do seu CPF após o hífen é: {primeiro_digito}')
cpf10 = cpf9 + str(primeiro_digito)

#Cálculo segundo dígito do CPF
regressiva = 11
soma = 0
for i in cpf10:
    soma += int(i) * regressiva
    regressiva -= 1
segundo_digito = (soma * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
print(f'O segundo digito do seu CPF é: {segundo_digito}')
print(f'O seu CPF inteiro é: \033[32m{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}-{primeiro_digito}{segundo_digito}\033[m')