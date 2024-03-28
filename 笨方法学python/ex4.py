cars = 100  

space_in_a_car = 4.0  # 每辆车的空间

drivers = 30         # 司机数量

passengers = 90      # 乘客数量

cars_not_drive = cars - drivers    # 没有司机的车

cars_driven = drivers              #  有司机的车

carpool_capacity = cars_driven * space_in_a_car     #  车的容量

average_passengers_per_car = passengers / cars_driven   # 每辆车的平均乘客数    

print("There are", cars, "cars avaliable.")

print("There are only", drivers, "drivers avaliable.")

print("There will be", cars_not_drive, "empty cars today.")

print("We can transport", carpool_capacity, "people today.")

print("We have",passengers, "to carpool today.")

print("We need to put about",average_passengers_per_car, "in each car.")
