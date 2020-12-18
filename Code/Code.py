def menu_display(menu_1,menu_burger_price,menu_2,menu_2_1,menu_steaks_price):
    print(f'{"Burgers":>30}')
    for burger in range(len(menu_1)):
        print(burger+1,end='  ')
        print(menu_1[burger],end=' ')
        print(f'{menu_burger_price[burger]:>20}/-')
    print(f'{"Steaks":>30}')
    print(menu_2[0])
    for steaks in range(len(menu_steaks_price)):
        print(steaks+1,end='  ')
        print(menu_2_1[steaks],end=' ')
        print(f'{menu_steaks_price[steaks]:>20}/-')
        print(menu_2[steaks+1])
def Burgers(menu_1,menu_burger_price):
    file_system = open('hassan.txt', 'w')
    choose_item = []
    while True:
        print('Choose the item from the menu list.', end=' ')
        choose_item += [input(':')]
        character = input('Enter for stop (N \ no) and continue (a--z \ A--Z) : ')
        if character == 'N':
            break
        elif character == 'no':
            break
    menu_item = [];
    menu_price = 0;
    for out, outs in enumerate(choose_item):
        print(out + 1, end=' ')
        print(outs, end=' ')
        for search in range(len(menu_1)):
            if menu_1[search] == choose_item[out]:
                print(menu_burger_price[search])
                menu_item += [menu_1[search]]
                menu_price += menu_burger_price[search]
    print("Enter the quantity (1 \ 2).", end=' ')
    quantity = int(input(':'))
    if quantity == 2:
        for dish_index, dish_item in enumerate(menu_item):
            print(dish_index + 1, end=' ')
            print(dish_item)
            file_system.write(str(dish_index + 1))
            file_system.write(f'  {dish_item}')
            file_system.write('\n')
        print('The total price of dish is {}'.format(menu_price))
        file_system.write('\n')
        file_system.write('The total price of dish is {}'.format(menu_price))
    elif quantity == 1:
        for dish_index1, dish_item1 in enumerate(menu_item):
            print(dish_index1 + 1, end=' ')
            print(dish_item1)
            file_system.write(str(dish_index1 + 1))
            file_system.write(f'  {dish_item1}')
            file_system.write('\n')
        print("The total price of dish with tax service charge is {}".format(menu_price + 400))
        file_system.write('\n')
        file_system.write('The total price of dish with tax service charge is {}'.format(menu_price + 400))

def Steaks(menu_2_1, menu_steaks_price):
    file_system = open('hassan.txt', 'w')
    choose_item = []
    while True:
        print('Choose the item from the menu list.', end=' ')
        choose_item += [input(':')]
        character = input('Enter for stop (N \ no) and continue (a--z \ A--Z) : ')
        if character == 'N':
            break
        elif character == 'no':
            break
    menu_item = [];
    menu_price = 0;
    for out, outs in enumerate(choose_item):
        print(out + 1, end=' ')
        print(outs, end=' ')
        for search in range(len(menu_2_1)):
            if menu_2_1[search] == choose_item[out]:
                print(menu_steaks_price[search])
                menu_item += [menu_2_1[search]]
                menu_price += menu_steaks_price[search]
    print("Enter the quantity (1 \ 2).", end=' ')
    quantity = int(input(':'))
    if quantity == 2:
        for dish_index, dish_item in enumerate(menu_item):
            print(dish_index + 1, end=' ')
            print(dish_item)
            file_system.write(str(dish_index + 1))
            file_system.write(f'  {dish_item}')
            file_system.write('\n')
        print('The total price of dish is {}'.format(menu_price))
        file_system.write('\n')
        file_system.write('The total price of dish is {}'.format(menu_price))
    elif quantity == 1:
        for dish_index1, dish_item1 in enumerate(menu_item):
            print(dish_index1 + 1, end=' ')
            print(dish_item1)
            file_system.write(str(dish_index1 + 1))
            file_system.write(f'  {dish_item1}')
            file_system.write('\n')
        print("The total price of dish with tax service charge is {}".format(menu_price + 400))
        file_system.write('\n')
        file_system.write('The total price of dish with tax service charge is {}'.format(menu_price + 400))


def choose_user(menu_1,menu_burger_price,menu_2,menu_2_1,menu_steaks_price):
    # Display the information about restaurant menu
    menu_display(menu_1, menu_burger_price, menu_2, menu_2_1, menu_steaks_price);
    print('\n\n')
    while True:
        print('1:\t BURGERS\n')
        print('2:\t STEAKS\n')
        print('3:\t EXIT\n')
        enter_user = int(input('Enter the number : '))
        if enter_user == 1:
            print('\n\n------------------------------ Burgers -----------------------------\n\n')
            Burgers(menu_1, menu_burger_price);
            print('\n\n')
        elif enter_user == 2:
            print('\n\n------------------------------- Steaks -----------------------------\n\n')
            Steaks(menu_2_1, menu_steaks_price);
            print('\n\n')
        elif enter_user == 3:
            print("\t\t\tThanks.Have a nice day sir/ms\n")
            exit(2)

if __name__ == '__main__':
    menu_1 = ['Zinger Burger', 'Zinger Cheese Burger', 'Thames Special Burger', 'Beef Burger'
        , 'Tower Burger', 'Fish Burger', 'Fish Cheese Burger', 'Fire Stone Burger', 'Crispy Burger'
        , 'Chicken Burger', 'Tikka Burger', 'Shami Burger']
    menu_burger_price = [230, 260, 320, 250, 320, 260, 290, 170, 170, 180, 170, 170]
    menu_2 = ['Beef or Chicken |- all steaks served with fries & vegetable',
              '(Char grilled beef or chicken topped with spicy American sauce)',
              '(Tender line Char grilled beef or chicken topped with creamy mushroom sauce)',
              '(Tender line beef or chicken medallion grilled topped with pepper corn sauce)',
              '(Char grilled steak topped with chef special sauce and slice cheese)']
    menu_2_1 = ['Arizona Steak', 'Mushroom Steak', 'Pepper Steak', 'Polo Tuscany']
    menu_steaks_price = [650, 650, 650, 650]
    choose_user(menu_1, menu_burger_price, menu_2, menu_2_1, menu_steaks_price);

