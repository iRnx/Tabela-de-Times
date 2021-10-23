lista1 = list()
lista2 = list()
while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(int(input('Vitória: ')))
    lista1.append(int(input('Empate: ')))
    lista1.append(int(input('Derrota: ')))
    lista2.append(lista1[:])
    lista1.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"Nome":<11} {"Vitória":<12} {"Empate":<11} {"Derrota":<11}')
for c in lista2:
    nome, vitoria, empate, derrota = c
    print(f'{nome:<14} {vitoria:<12} {empate:<11} {derrota}')
    