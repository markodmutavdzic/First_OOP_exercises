# 1. Create a Vehicle class with max_speed and mileage instance attributes.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage


# 2.Create a Vehicle class without any variables and methods.

# class Vehicle:
#     pass


# 3.Create a child class Bus that will inherit all of the variables and methods of the
# Vehicle class and display class attributes.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# class Bus(Vehicle):
#     def __str__(self):
#         return f'Vehicle max speed is {self.max_speed} and mileage is {self.mileage:,} miles.'

# 4.Create a Bus class that inherits Vehicle class. Vehicle class must have a seating_capacity method implemented.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f' Vehicle capacity is : {capacity}'
#
# class Bus (Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)


# 5.Define a class attribute color with a default value of white. I.e. Every Vehicle should be white.

# class Vehicle:
#     color = 'White'
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage


# 6.Create a Bus child class that inherits from the Vehicle class.
# The default charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So the total fare for Bus instance will become the final amount = total fare + 10% of the total fare.
# The Bus seating capacity is 50, so the final fare amount should be 5500.
# Implement fare method on Vehicle class and do necessary modifications on Bus class for the same method.


# class Vehicle:
#     color = 'White'
#
#     def __init__(self, max_speed, mileage, capacity):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.capacity=capacity
#
#
#     def total_fare(self):
#         return self.capacity*100
#
# class Bus (Vehicle):
#     def total_fare(self):
#         return super().total_fare()*1.1


# 7.Check if school_bus variable is also an instance of the Vehicle class.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
# class Bus(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 12, 50)
#
#
# print(isinstance(School_bus,Vehicle))
