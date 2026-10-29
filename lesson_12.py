# abc = [1, 123, 578, 234, 436, 235, 856, 798, 7598, 2435, 586]
# for x in abc:
#     print(x * 10)
# abc.append(100)
# a = abc.pop(1)
# abc.sort()
# a = abc.index(234)
# abc.clear()
# print(a)


abc = [1, 123, 578, 234, 436, 235, 856, 798, 7598, 2435, 586]
numbers = []
total = 0
fruits = []
for x in abc:
    if x > 500:
        numbers.append(x)
    elif x < 500:
        fruits.append(x)
        total = x + total

print(numbers)
print(fruits)
print(total)

for x in numbers:
    if x < 900:
        numbers.remove(x)   

print(numbers)
