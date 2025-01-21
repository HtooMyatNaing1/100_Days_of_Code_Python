print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pizza_price = 0

if size.lower() == "s":
    pizza_price += 15
    # print(f"A small sized pizza costs ${pizza_price}.")
    if pepperoni.lower() == "y":
        pizza_price += 2
        # print(f"With pepperoni, your pizza is ${pizza_price}.")

elif size.lower() == "m":
    pizza_price += 20
    # print(f"A medium sized pizza costs ${pizza_price}.")
    if pepperoni.lower() == "y":
        pizza_price += 3
        # print(f"With pepperoni, your pizza is ${pizza_price}.")

elif size.lower() == "l":
    pizza_price += 25
    # print(f"A large sized pizza costs ${pizza_price}.")
    if pepperoni.lower() == "y":
        pizza_price += 3
        # print(f"With pepperoni, your pizza is ${pizza_price}.")

else:
    print("Please enter only given options.")

if extra_cheese.lower() == "y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")

