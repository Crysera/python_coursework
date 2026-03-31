# 21Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
work = int(input("enter hours : "))
time = int(input("enter rate per hour :"))
pay = work*time 
print(f"your weekly earnings is {pay}")
# 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years  = int(input("enter numbers of years you have lived :"))
totaltime = 365 * 24 * 60 * 60
live = years * totaltime
print(f"You have lived for {live} seconds.  ")

# 23Write a Python script that displays the following table
print("1 1 1 1 1")
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)