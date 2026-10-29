# n1 = int(input("Please enter first number:  "))
# n2 = int(input("Please enter second number:  "))
# q = 0
# for x in range(n1, n2 + 1):
#     q = q + x

# print("The sum of all the numbers is: ", q)


# a = 1
# b = 2
# abc = [1, 123, 578, 234, 436, 235, 856, 798, 7598, 2435, 586]
# for x in abc:
#     if 200 < x < 300:
#        print(x)
# abc.append(100)
# a = abc.pop(1)
# abc.remove(234)
# print(abc)

# fruits = ["apple", "banana", "pineapple", "orange", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple",]
# fruits.extend(abc)
# fruits.insert(3, 100)
# fruits.clear()
# a = fruits.index("apple")
# a = fruits.count("pineapple")
# print(a)


# less_then_500 = []
# more_then_500 = []
# abc = [1, 123, 578, 234, 436, 235, 856, 798, 7598, 2435, 586, 423, 15426, 634, 436478, 3467,24653, 637, 4, 23546, 546, 347, 347, 34]
# for x in abc:
#     if x < 500:
#         less_then_500.append(x)
#     else:
#         more_then_500.append(x)

# print(less_then_500)
# print(more_then_500)

l = []
for x in range(5):
    n1 = int(input("Please enter your number:  "))
    l.append(n1)

print(l)