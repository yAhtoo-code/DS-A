import os
def clear_screen():
    input("\nPress Enter to continue...")
    os.system("cls")

print("Shopping Cart Inventory")
print("--------------------------------------------------")
number_of_carts = int(input("How many carts do you want to input?\n"))
clear_screen()

carts = {}

for i in range(1, number_of_carts + 1):
    cart_id = input(f"Enter Cart ID for cart {i}: ")

    ItemPrice1 = float(input("Enter Item 1 Price: "))
    ItemQty1 =  int(input("Enter Item 1 Quantity: "))
    ItemPrice2 = float(input("Enter Item 2 Price: "))
    ItemQty2 =  int(input("Enter Item 2 Quantity: "))
    ItemPrice3 = float(input("Enter Item 3 Price: "))
    ItemQty3 =  int(input("Enter Item 3 Quantity: "))
    clear_screen()

    carts[cart_id] = {
        "ItemPrice1": ItemPrice1, "ItemQty1": ItemQty1, 
        "ItemPrice2": ItemPrice2, "ItemQty2": ItemQty2,
        "ItemPrice3": ItemPrice3, "ItemQty3": ItemQty3
    }

#Formula Total = (Item1 * Qty1) + (Item2 * Qty2) + (Item3 * Qty3) 
print("Challenge Questions")
print("-----------------------------------------")
print("1.) Compute the Total for CartID 201.")
first_cart_id = list(carts.keys())[0]
cart1 = carts[first_cart_id]  
total1 = (cart1["ItemPrice1"] * cart1["ItemQty1"] +
          cart1["ItemPrice2"] * cart1["ItemQty2"] +
          cart1["ItemPrice3"] * cart1["ItemQty3"])
print(f"The Total of Cart {first_cart_id} is {total1}")
print("")

print("2.) Which CartID has the most expensive cart?")
highest_cart_name = None
highest_total = 0
sum_of_totals = 0

for cart_id_name, items in carts.items():
    total = (items["ItemPrice1"] * items["ItemQty1"] +
             items["ItemPrice2"] * items["ItemQty2"] +
             items["ItemPrice3"] * items["ItemQty3"])
    print(f"The Total of {cart_id_name} is {total}")
    print("")

    sum_of_totals += total

    if total > highest_total:
        highest_total = total
        highest_cart_name = cart_id_name

print(f"The most expensive cart is {highest_cart_name} with a total of {highest_total}")
print("")

print("3.) What is the average cart total?")
average_total = sum_of_totals / number_of_carts
print(f"The average cart total is {average_total:.2f}")
print("")



