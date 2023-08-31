print('Converting USD into Pounds')

convert_to_pounds = lambda dollars: dollars * 0.82
dollars = int(input('Enter Dollars: '))
pounds = convert_to_pounds(dollars)

print(f'{dollars} Dollars = {pounds} Pounds')