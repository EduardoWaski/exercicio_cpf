import random
cpf_usuario = ''
for b in range(9):
     cpf_usuario += str(random.randint(0, 9))
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
print(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}-{primeiro_digito}{segundo_digito}')