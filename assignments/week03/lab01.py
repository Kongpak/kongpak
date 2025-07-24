# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter your age: "))
if age <= 12:
    print("You are Child")
elif age <= 19:
    print("You are Teenager")
elif age <= 59:
    print("You are Adult")
elif age >= 60:
    print("You are Senoir")
else:
    print("Invalid age")