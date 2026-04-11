## question 1 - 7

# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
age = 23
height = 165.1
number = 1 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input(" enter base :"))
height = float(input(" enter height :"))
area = 0.5 * base * height 
print(f" the area of the triangle is :{int(area)}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("enter side a : "))
b = float(input("enter side b : "))
c = float(input("enter side c : "))
perimeter = a + b + c
print(f" the perimeter of the triangle is :{perimeter}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght = float(input(" enter length :"))
bredth = float(input(" enter bredth :"))
area = lenght * bredth
perimeter = 2*(lenght + bredth)
print(f"the area of the triangle is : {area}")
print(f"the perimeter of the triangle is : {perimeter}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("enter the radius of the circle :"))
pi = 3.14
area = pi*radius**2
circumference = 2*pi*radius
print(f"the area of the circle is :{area}")
print(f"the circumference of the circle is : {circumference}")


