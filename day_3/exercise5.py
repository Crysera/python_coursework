# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# 19 Check if type of '10' is equal to type of 10
# 20Check if int('9.8') is equal to 10

#18
floor_devision = 7 // 3
print(floor_devision)

if int(2.7) == floor_devision:
    print(True)
else:
    print(False)

#19
num = '10'
num1 = 10
if type(num) == type(num1):
    print(True)
else:
    print(False)

#20
num = 10
num1 = '9.8'
converted_num1 = int(float(num1))
if converted_num1 == num:
    print(True)
else:
   
    print(False)