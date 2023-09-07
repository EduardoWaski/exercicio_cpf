cpf_usuario = input('Digite o seu CPF: ')
cpf = ''
for digito in cpf_usuario:
    if digito.isdigit() == False:
        continue
    else:
        cpf += digito
cpf9 = cpf[:9]
regressiva = 10
soma = 0
for numero in cpf9:
    mult = int(numero) * regressiva
    soma += mult
    regressiva -= 1

digito1 = (soma * 10) % 11
primeiro_digito = digito1 if digito1 <= 9 else 0 
cpf10 = cpf9 + str(primeiro_digito)

regressiva = 11
soma = 0
for i in cpf10:
    soma += int(i) * regressiva
    regressiva -= 1
segundo_digito = (soma * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
if cpf10 + str(segundo_digito) == cpf10[0] * 11:
     print('\033[31mCPF inválido\033[m')
elif cpf10 + str(segundo_digito) == cpf:
        print('\033[32mCPF válido\033[m')
else:
    print('\033[31mCPF inválido\033[m')
