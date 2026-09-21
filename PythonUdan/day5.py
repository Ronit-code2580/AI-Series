# num = -1
# if num > 0:
#     print("The number is positive")
# else:
#     print("The number is negative")

# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is positive")
# else:
#     print("The number is negative")  

# if -> else if (elif) .....................-> else
'''
if condition:
    statements(s)
elif condition:

    statements(s)
....
else:
    statements(s)

'''
# num = int(input("Enter a number: "))

# if num == 0:
#     print("The number is zero")

# elif num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# re = num / 2;
# print(re)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

ch = int(input("Enter:\n1. for addition\n2. for subtraction \n3. for product\n "))
'''
num1 > num2:
   num1 > num3:
   print("The greates number is: ) //num1

   else:
   print("The greates number is: ") //num3
 else 
    num2 > num3L
    print("The greates number is: ") //num2

'''
# if (num1 > num2) and (num1 > num3):
#         print("The greatest number is: ", num1)
# elif (num2 > num1) and (num2> num3):
#         print("The greatest number is: ", num2)
# else:
   
#         print("The greatest number is: ", num3)

#-------------------task 1---------------
#add, sub, pro
match ch:
    case 1:
        add = num1 + num2
        print(f"{num1} + {num2} = {add}")
    case 2:
        if num1 > num2:
            sub = num1 - num2
            print(print(f"{num1} - {num2} = {sub}"))
        else:
            sub = num2 - num1
        print(print(f"{num2} - {num1} = {sub}"))
    case 3:
        pro = num1 * num2
        print(f"{num1} X {num2} = {pro}")
    case _:
        print("Invalid choice")

