def calculate_discount(price, discount_percent):
    if discount_percent < 0.2:
        return "item cost:$" + str(price)
    else:
        discount = price * discount_percent
        final_price = price - discount
        return f'item cost:${final_price}'
pay = calculate_discount(int(input("Enter price: ")), float(input("Enter discount: ")))
print(pay)









