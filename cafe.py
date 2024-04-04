
"""
This program calculates the total stock worth of the cafe.
The menu list has 8 items currently sold.
The price and stock dictionaries give the price and stock number of each item
stock value is calculated by item_value = (stock[items]) * price[items])
"""


menu = [
    "Espresso",
    "Cappuccino",
    "Green Tea",
    "Iced Coffee",
    "Croissant",
    "Muffin",
    "Bagel with Cream Cheese",
    "Avocado Toast"
]
price = {
    "Espresso": 2,
    "Cappuccino": 2,
    "Green Tea": 1.5,
    "Iced Coffee": 1.8,
    "Croissant": 3,
    "Muffin": 3,
    "Bagel with Cream Cheese":2.5,
    "Avocado Toast": 4
    }
stock = {
    "Espresso":45,
    "Cappuccino":20,
    "Green Tea":54,
    "Iced Coffee":78,
    "Croissant":45,
    "Muffin":30,
    "Bagel with Cream Cheese":35,
    "Avocado Toast":74
}

stock_value = [a*b for a,b in zip(price.values(), stock.values())] # create a list of the total value of each item
total_stock = sum(stock_value) # calculate the total value

print(f"The total stock value of all the items sold in the cafe is {total_stock} pounds.")
