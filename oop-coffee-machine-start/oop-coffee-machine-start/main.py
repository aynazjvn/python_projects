from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso",100,0,16,1.5)
latte = MenuItem("latte",200,150,24,2.5)
cappuccino = MenuItem("cappuccino",250,100,24,3.0)

off = False
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not off:
    choice = input(f"What would you like? {menu.get_items()}:")

    if choice == "off":
        off = True

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        order = (menu.find_drink(choice))
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)




