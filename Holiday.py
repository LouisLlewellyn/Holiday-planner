# Holiday planner

# Dictionarys
flight_cost = {"madagascar" : 589,
                "mauritius" : 647,
                "seychelles" : 745,
                "reunion" : 497
                }

hotel_cost = {"madagascar" : 120,
              "mauritius" : 150,
              "seychelles" : 175,
              "reunion" : 90
              }

car_cost = {"large family car" : 35,
            "small family car" : 28,
            "sports car" : 39,
            "city car" : 24}

# Flight cost function
def flight_func(flight_cost, people):
    return flight_cost.get(city_flight.lower()) * people

# Hotel cost function
def hotel_func(hotel_cost, rooms, nights):
    return (hotel_cost.get(city_flight.lower()) * rooms) * nights

# Car cost function
def car_func(car_cost, days):
    return car_cost.get(type_car.lower()) * days

# Holiday total cost
def total_cost(flight_total, hotel_total, car_total):
    return flight_total + hotel_total + car_total

while True:
    print("=============================================================================")
    print("                     Welcome to LL's holiday planner")
    print("=============================================================================")
    print("We are currently offering deals to", ", ".join([key.capitalize() for key in flight_cost.keys()]))
    print("-----------------------------------------------------------------------------\n")

# Number of people
    while True:
        people_num = input("Select the number of people who are going: ")

        try:
            people = int(people_num)
            
            if people == 0:
                print("\nZero people can't go on holiday!!")
            else:
                break
        except ValueError:
            print("\nWe need a number!")            

# Destination
    while True:
        city_flight = input("Select the destination you would like to fly to: ")

        if city_flight.lower() in flight_cost:
            print(f"\nGreat choice. We love {city_flight.capitalize()}!")
            break
        else:
            print("\nOops! We didn't recognise that. Please enter a destination from our deals list.")

    if city_flight.lower() in flight_cost:

        flight_total = flight_func(flight_cost,people)        # Flight total cost

        print("-----------------------------------------------------------------------------")
        print(f"        A return flight to {city_flight.capitalize()} for {people} people is currently £{flight_total:.2f}")
        print("-----------------------------------------------------------------------------\n")
       
# Number of nights
    while True:
        num_nights = input("How many days would you like to stay at the hotel: ")

        try:
            nights = int(num_nights)
            
            if nights == 0:
                print("\nYou can't stay in the hotel for zero days!!")
            else:
                break
        except ValueError:
            print("\nWe need a number!")

    while True:
        num_rooms = input("How many rooms would you like: ")

        try:
            rooms = int(num_rooms)
            if rooms == 0:
                print("\nWhere will you sleep!?!")
            else:
                break
        except ValueError:
            print("\nWe need a number!")
        
    hotel_total = hotel_func(hotel_cost, rooms, nights)      # Hotel total cost

    print("-----------------------------------------------------------------------------")
    print(f"     A stay in our {city_flight.capitalize()} hotel for {nights - 1} nights with {rooms} room(s) is £{hotel_total:.2f}")
    print("-----------------------------------------------------------------------------\n")
        
# Car rental
    while True:
        car = input("Would you like to higher a car (Y/N): ")

        try:
            if car.lower() in ["y","n"]:
                break
            else:
                print("\nWe need a yes(Y) or a no(N)!")    
        except ValueError:
            print("\nWe need a yes(Y) or a no(N)!")

    if car.lower() == "y":
        print("------------------------------------------------------------------------------")
        print(f"             We have a range of hire cars available in {city_flight.capitalize()}:\n         ", ", ".join([key.capitalize() for key in car_cost.keys()]))
        print("-----------------------------------------------------------------------------\n")

        while True:
            type_car = input(f"What type of car would you like: ")
         
            if type_car.lower() in car_cost:
                break   
            else:
                print("\nOops! We didn't recognise that. Please enter the type of car from the hire list.")
        while True:
            car_days = input(f"How many days would you like to hire the {type_car.lower()} for: ")

            try:
                days = int(car_days)
                break
            except ValueError:
                print("\nWe need a number!")
            
        car_total = car_func(car_cost, days)      # Car total cost

        print("-----------------------------------------------------------------------------")
        print(f"        To hire a {type_car.capitalize()} in {city_flight.capitalize()} for {days} days will cost £{car_total:.2f}")
        print("-----------------------------------------------------------------------------\n")

        print("That's everything we need to proceed with your booking today.")
                  
        holibobs_total = total_cost(flight_total, hotel_total, car_total)      # Holiday total cost

        print("----------------------------------------------------------------------------")
        print(f"            The total cost of your holiday will be £{holibobs_total:.2f}.")    
        print("----------------------------------------------------------------------------")

    if car.lower() == "n":
        print("----------------------------------------------------------------------------")
        print(f"        No problem. There is plenty of public transport around {city_flight.capitalize()}.")
        print("----------------------------------------------------------------------------")

        print("\nThat's everything we need to proceed with your booking today.")
             
        holibobs_total = total_cost(flight_total, hotel_total, car_total = 0)       # Holiday total cost, without car rental

        print("-----------------------------------------------------------------------------")
        print(f"             The total cost of your holiday will be £{holibobs_total:.2f}.")
        print("----------------------------------------------------------------------------\n")

# Start from beginning
    while True:
        start = input("Would you like to start again (Y/N): ")
        
        try:
            if start.lower() in ["y","n"]:
                break
            else:
                print("\nWe need a yes(Y) or a no(N)!")    
        except ValueError:
            print("\nWe need a yes(Y) or a no(N)!")

    if start.lower() == "n":
        break
    else:
        print("\n-----------------------------------------------------------------------------")

print()
print("==============================================================================")
print("                    Thanks for using LL's Holiday Planner")
print("==============================================================================")
