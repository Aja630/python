# 1.conditional:- if,if-else,if-elif,if-elif-else
# 2.iterative:- while, for 
# 3.transfer:- continue, break, pass

#1. if=> syntax:-
#             if condition:

# if                  
# x=10
# if x>=15:
#     print("welcome to if body")
# print("welcome to main body")


# x=input("Enter any thing")
# x=False
# if x:
    # print("Hello")
    # print("-----")



# 2.if-else=>  
# syntax:
#           if condition: true or false
#         statement 1

#         else:
#               statement 2

# if-else
# Q.1 WAP  to check given no. is even or odd
# n= int(input("enter any number"))
# if n%2==0:
#     print(f'given no{n} is even')
# else:
#     print(f'given no{n} is odd')


# //if-elif
# x=(input("enter any number"))
# y=(input("enter any number"))
# z=(input("enter any number"))
# if (x>y and x>z):
#     print(x)
# elif (y>x and y>z):
#     print(y)
# else:
#     print(z)



# //if-elif-else
# x=(input("enter any number"))
# y=(input("enter any number"))
# z=(input("enter any number"))
# if (x>y and x>z):
#     print(f'{x} is greater')
# elif (y>x and y>z):
#     print(f'{y} is greater') 

# else:

#     print(f'{z} is greater')


x=(input("enter any number"))
y=(input("enter any number"))
z=(input("enter any number"))
if (x>y and x>z):
    print(f'{x} is greater')
elif (y>x and y>z):
    print(f'{y} is greater') 

else:

    print(f'{z} is greater')



# Iterative looping statement

# while (infinite ,iteration)
# for  ( finite iteration)
  