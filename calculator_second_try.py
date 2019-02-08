# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

def add1(x, y, z):
   return x + y + z 

def add2(x, y, z, t):
   return x + y + z + t 


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")



# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice == '1':
   choice1 = int(input("How many numbers would you like to add?(2/3/4): "))
   print(choice1)
   """"
      Choice is of type int by default. Since you dont have an explicit cast the default type for 
      storing numbers is int. Change all of the if conditions to compare with number rather than string
   """"
   if choice1 == 2:
      print("%d+%d=%d",num1,num2, add(num1,num2))  
   elif choice1 == '3': 
      num3 = int(input('Enter third number: '))
      print(num1,"+",num2, "+", num3, "=", add1(num1,num2,num3))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
