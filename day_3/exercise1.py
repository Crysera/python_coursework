#question 8 ,9 ,10

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2  # Slope
c = -2 # y-intercept (the constant)

# 2. Python calculates the y-intercept
# The y-intercept occurs when x = 0
# y = m * 0 + c -> y = c
y_intercept = c

# 3. Python calculates the x-intercept
# The x-intercept occurs when y = 0
# 0 = mx + c  =>  -c = mx  =>  x = -c / m
x_intercept = -c / m

print(f"Slope (m): {m}")
print(f"Calculated Y-intercept: {y_intercept}")
print(f"Calculated X-intercept: {x_intercept}")

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2,2
x2, y2 = 6,10
m1 = (y2-y1)/(x2-x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(m1)
print(distance)

#Compare the slopes in tasks 8 and 9.
print(m == m1)
