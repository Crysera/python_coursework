# 16 Find the length of the text python and convert the value to float and convert it to string
text = " python"

length = len(text)
print(f"the length: {length}", type(length))

float_length = float(len(text))
print(f"converted float value : {float_length}",type(float_length))

str_length = str(len(text))
print(f"converted to string : {str_length}",type(str_length))

# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("enter a number : "))
if number % 2 == 0:
    print("the number is divisible ")
else:
    print("not divisible")


