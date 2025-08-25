cod_one, unit_one, price_one = input().split()
cod_two, unit_two, price_two = input().split()

int_unit_one = int(unit_one)
float_price_one = float(price_one)
int_unit_two = int(unit_two)
float_price_two = float(price_two)

price_full = (int_unit_one * float_price_one + int_unit_two * float_price_two)
print(f'VALOR A PAGAR: R$ {price_full:.2f}')
