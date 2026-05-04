# user input section
first_name =input("enter your name : ")
daily_step_goal =int(input("enter your daily step goal :"))
actual_steps = int(input("enter your actual steps taken today :"))

# arithmatic operation 
goal_short =  (daily_step_goal - actual_steps)
print(goal_short)

if daily_step_goal == actual_steps:
    print("met")
elif daily_step_goal < actual_steps:
    print("exceeded")
else : 
    print("daily goal requirement not met ")

if actual_steps / 2 > 0 :
    print("they took even number of steps !! ")