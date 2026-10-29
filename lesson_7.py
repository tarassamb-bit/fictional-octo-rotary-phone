# for x in range(3):
#     print('Hello')
# for x in range(4):
#     print('Ok')
# for x in range(5):
#     print('Test')

# n1 = int(input())
# n2 = int(input())
# add = 0
# for x in range(n1, n2 + 1):
#     add = add + x
#     print(x)
# print("Sum of the numbers:  ", add )

# for x in range(0, 100 + 1, 2):
#     print(x)

# for x in range(5):
#     for a in range(1, 6):
#         print(a)

# while 100 == 100:
#     print("HELLO")


# x = 0
# while x < 5:
#     print(x)
#     x = x + 1

name = input("Enter your name:  ")
while name == '':
    print("You didn't enter your name. Please try again.")
    name = input("Enter your name:  ")
print("Hello, ", name)