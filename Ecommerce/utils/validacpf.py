import re

def valida_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', str(cpf))  # Remove tudo que não for número

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False  # Verifica se tem 11 dígitos e não são todos iguais

    novo_cpf = cpf[:9]
    reverso = 10
    total = 0

    for i in range(19):
        total += int(novo_cpf[i % 9 if i < 9 else i - 9]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            digito = digito if digito < 10 else 0
            novo_cpf += str(digito)
            total = 0

    return cpf == novo_cpf
