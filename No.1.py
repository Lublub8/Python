print("Python Cafe")
print("-" * 30)

menu = {'Brownie': 2.5,
        'Croissant': 3,
        'Chocolate Cookie': 2.75,
        'Latte': 12.5,
        'Hot Chocolate': 12}

for food, price in menu.items():
    print(f'{food:15} USD {price}')

bill = 0

order = input("Kindly place your Order:\n").title()

if order in menu.keys():
    try:
        for menu, price in menu.items():
            if menu == order:
                bill += price

    except:
        print(f'Sorry, Wrong Order!! We do not sell {order}')

    else:
        quantity = int(input(f'How Many {order}s do you wish to Order?\n'))

print('-' * 30)
print(f'The Total Bill Amount is $ {bill * quantity}')
