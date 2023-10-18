# Estações do ano

#Apresentação
print('\n\t\t\t -- Estações do Ano -- \n\n')

# Entradas
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))

# Processamento e Saída
if mes == 1 or mes == 2 or mes == 3:
    print('\nVerão\n')
elif mes == 4 or mes == 5 or mes == 6:
    print('\nOutono\n')
elif mes == 7 or mes == 8 or mes == 9:
    print('\nInverno\n')
elif mes == 10 or mes == 11 or mes == 12:
    print('\nPrimavera\n')