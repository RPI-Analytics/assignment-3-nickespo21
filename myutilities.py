def divby2(n):
    n = [i for i in n if i % 2 == 0]
    return n

numbers = [3, 12, 91, 33, 21, 34, 54, 34, 34, 54]
divby2=divby2(numbers)
print(divby2)