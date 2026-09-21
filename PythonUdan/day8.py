# Error
# print("Hello World ) -> Syntax error

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))

# sum = num1 - num2 # This represents logical error
# print(f"sum = {sum}")

#Exceptions 
# x = int(input("Enter a number: "))
# print(x) - > to demonstrate ValueError

# try:
#     x = int(input("Enter a number: "))

# except ValueError:
#     print("Please Enter an Integer!!")
    
# print(f"number = {x}")

# try:
#     x = int(input("Enter a number: "))

# excep
# except ValueError:
#     print("Please Enter an Integer!!")

# else:
#     print(f"number = {x}")


'''
try:



except:
.......
.......
.......

else: 

finally: 


'''
# try:
#     x = int(input("enter a number: "))
#     # print(f"number = {x}")

# except ValueError:
#     print("Please enter an integer")

# else:
#     print(f"number = {x}")

#task 

# while True:
#     try: 
#         x = int(input("enter a number: "))
    
#     except ValueError:
#         print("Please enter an integer")
#     else:
#         print(f"number = {x}")
#     break
# while True:
#     try:
#           x = int(input("enter a number: "))
#           result = 10/x
#     except ValueError:
#      print("Please Enter an Integer")
#     except ZeroDivisionError:
#      print("Cannot divide by zero")
#     else:
#      print(f"Result = {result}")
#      break

# def main():
#     x = get_int()
#     print(f"number = {x}")
# def get_int():
#     while True:
#         try:
#             x = int(input("enter a number: "))
#         except ValueError:
#             pass
#         else:
#             return x
# main()
# while True:
#     try:
#       num1 = int(input("Enter a numeber: "))
#       num2 = int(input("Enter another number: "))
#       num3 = int(input("Enter another number: "))

#       operation = (num1+num2)/num3

#     except ValueError:
#       pass
#     except ZeroDivisionError:
#       pass
#     else:
#       sum = num1 + num2 + num3
#       product = num1 * num2 * num3
#       print(f"sum = {sum}")
#       print(f"product = {product}")
#       print(f"operation = {operation}")
#       break
    
  
while True:
      try:
         num5 = int(input("enter a number: "))

      except ValueError:
         print("enter a integer")
      
      
      break
print(num5)