from fun_folder.test import miles

print(miles(3,9))

# 1.1 Part A

print("This program calculates Celsius")

temperature_in_fahrenheit = input("Enter temperature in Farenheit:")
temperature_in_fahrenheit = float (temperature_in_fahrenheit)

temperature_in_celsius = float ((temperature_in_fahrenheit) - 32) * 5/9
print("Temperature in Celsius", temperature_in_celsius)


# 1.2 Part B

print("This Program calculates the Area of a Trapezoid")

trapezoid_height = input("Enter height:")
trapezoid_height = float(trapezoid_height)
trapezoid_bottom_base_length = input("Enter bottom base length:")
trapezoid_bottom_base_length = float(trapezoid_bottom_base_length)
trapezoid_top_base_length = input("Enter top base length:")
trapezoid_top_base_length = float(trapezoid_top_base_length)

area = float ((trapezoid_top_base_length + trapezoid_bottom_base_length) / 2) * trapezoid_height
print("The area is:", area)

# 1.3 Part C

print("This Program calculates the Area of a Circle")

circle_radius = input("Enter circle radius:")
circle_radius = float(circle_radius)

circle_area = 3.14159 * (float(circle_radius * circle_radius))
print("The area is:", circle_area)

