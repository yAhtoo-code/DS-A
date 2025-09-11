cartID201 = {
    "ItemPrice1" : 100,
    "ItemQty1"   : 2,
    "ItemPrice2" : 50,
    "ItemQty2"   : 1,
    "ItemPrice3" : 30,
    "ItemQty3"   : 5,
}

cartID202 = {
    "ItemPrice1" : 200,
    "ItemQty1"   : 1,
    "ItemPrice2" : 80,
    "ItemQty2"   : 2,
    "ItemPrice3" : 40,
    "ItemQty3"   : 3,
}

cartID203 = {
    "ItemPrice1" : 150,
    "ItemQty1"   : 3,
    "ItemPrice2" : 70,
    "ItemQty2"   : 2,
    "ItemPrice3" : 25,
    "ItemQty3"   : 4,
}

cartID204 = {
    "ItemPrice1" : 250,
    "ItemQty1"   : 4,
    "ItemPrice2" : 90,
    "ItemQty2"   : 1,
    "ItemPrice3" : 35,
    "ItemQty3"   : 2,
}

cartID205 = {
    "ItemPrice1" : 300,
    "ItemQty1"   : 2,
    "ItemPrice2" : 60,
    "ItemQty2"   : 3,
    "ItemPrice3" : 20,
    "ItemQty3"   : 6,
}

carts = {
    "cartID201" : cartID201,
    "cartID202" : cartID202,
    "cartID203" : cartID203,
    "cartID204" : cartID204,
    "cartID205" : cartID205,
}
#Formula Total = (Item1 * Qty1) + (Item2 * Qty2) + (Item3 * Qty3) 

#Challenge Questions
#1.) Compute the Total for CartID 201.
cart1 = carts["cartID201"]  
total = (cart1["ItemPrice1"] * cart1["ItemQty1"] +
          cart1["ItemPrice2"] * cart1["ItemQty2"] +
          cart1["ItemPrice3"] * cart1["ItemQty3"])

print(f"The Total of Cart 201 is {total}")
print("")

#2.) Which CartID has the most expensive cart?
highest_cart_name = None
highest_total = 0
sum_of_totals = 0
cart_count = 0

for cart_id_name, items in carts.items():
    total1 = (items["ItemPrice1"] * items["ItemQty1"] +
             items["ItemPrice2"] * items["ItemQty2"] +
             items["ItemPrice3"] * items["ItemQty3"])
    print(f"The Total of {cart_id_name} is {total1}")
    print("")

    sum_of_totals += total1
    cart_count += 1

    if total1 > highest_total:
        highest_total = total1
        highest_cart_name = cart_id_name

print(f"The most expensive cart is {highest_cart_name} with a total of {highest_total}")
print("")

#3.) What is the average cart total?
average_total = sum_of_totals / cart_count
print(f"The average cart total is {average_total:.2f}")