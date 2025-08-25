nome_vendedor = input()
salario_fixo = float(input())
dinheiro_vendas = float(input())

total = salario_fixo + (dinheiro_vendas)*15/100

print(f'TOTAL = R$ {total:.2f}')
