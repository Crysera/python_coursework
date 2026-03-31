# 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x_values = [-5, -4, -3, -2, -1, 0]

print(f"{'x':<5} | {'y':<5} | {'Is y zero?'}")
print("-" * 25)

for x in x_values:
    # 1. Arithmetic Operators to calculate y
    y = x**2 + 6*x + 9
    
    # 2. Comparison Operator to check the condition
    is_zero = (y == 0)
    
    print(f"{x:<5} | {y:<5} | {is_zero}")

