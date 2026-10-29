# My Code

# c1 = input('Write first number:  ')
# c2 = input('Write second number:  ')
# c3 = input('Write add or multiply or divide or minus:  ')
# cc1 = int(c1)
# cc2 = int(c2)

# if c3 == 'add':
#     print(cc1 + cc2)
# else:
#     if c3 == 'multiply':
#          print(cc1 * cc2)
#     else:
#         if c3 == 'divide':
#             print(cc1 / cc2)
#         else:
#             if c3 == 'minus':
#                 print(cc1 - cc2)
#             else: 
#                 print("You didnt write what to do so:")
#                 print(cc1 - cc2)
#                 print(cc1 / cc2)
#                 print(cc1 * cc2) 
#                 print(cc1 + cc2)



cc1 = int(input('Write first number:  '))
cc2 = int(input('Write second number:  '))
c3 = input('Write add or multiply or divide or minus:  ')

if c3 == 'add':
    print(cc1 + cc2)
elif c3 == 'multiply':
    print(cc1 * cc2)
elif c3 == 'divide':
    print(cc1 / cc2)
elif c3 == 'minus':
    print(cc1 - cc2)
else:
    print("You didnt write what to do so:")
    print(cc1 - cc2)
    print(cc1 / cc2)
    print(cc1 * cc2) 
    print(cc1 + cc2)