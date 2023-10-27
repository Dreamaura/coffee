latte = 3.50
americano = 3
espresso = 2.5
count = 0


while True:
    coffee = input("What coffee would you like? 1. Latte €3.50, 2. American €3, 3. Espresso €2.50 ")
    if coffee.isnumeric():
        coffee = float(coffee)
        if coffee in [1, 2, 3]:
            break
    else:
        print("Please enter a valid item number.")

if coffee == 1:
    coffee = latte
elif coffee == 2:
    coffee = americano
else:
    coffee = espresso

while count < coffee:
    balance = input("please enter cash, €1 or €2. ")
    if balance.isnumeric():
        balance = float(balance)
        if balance in [1, 2]:
            print(f"You have inserted, {count + balance}")
            count = count + balance
    else:
        print("Only €1 and €2 allowed.")

change = count - coffee
print(f"Thank you, your change is, {change}")

