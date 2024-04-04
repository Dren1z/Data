'''
This program calculate the total cost of a holiday based on the city
the number of nights to stay and number of days to rent a car.
'''



# Dictionary of cities and their associated flight prices
flight_prices = {
    "New York": 450,
    "London": 550,
    "Tokyo": 800,
    "Paris": 500,
    "Sydney": 900,
    "Dubai": 600
} 


def hotel_cost (nights):
    return 243 * nights

def plane_cost (city):
    price  = flight_prices[city] # Choose the flight price
    return price*2

def car_rental(days):
    return 28*days

def holiday_cost():
    while True:
        city_flight = input("Choose the city you will be flying to \n(New York, London, Tokyo, Paris, Sydney, Dubai): ")
        if city_flight in flight_prices: # Check if the city entered is in the list
            break
        else:
            print("Invalid city. Please choose from the list.")

    num_nights = int(input("The number of nights you will be staying: "))
    rental_days = int(input("The number of days for which you will be hiring a car: "))

    hotelcost = hotel_cost(num_nights)
    planecost = plane_cost(city_flight)
    carrental = car_rental(rental_days)
    cost = hotelcost+planecost+carrental
    print(f"The total cost of the holiday will be {cost} GBP.")

holiday_cost()
