numbers = [1, 2, 3, 4, 5, 6]
print(numbers[3])               # zostanie wydrukowany 4 bo listę numerujemy od 0

numbers = [12, 6, 2, -5, 4]
numbers[1] = numbers[3] - 10
print(numbers[1])

numbers = [2, 5, 2, 10, 15, 6]
numbers.insert(3, 11)
print(numbers)          # [2, 5, 2, 11, 10, 15, 6]
numbers.append(4)
print(numbers)          # [2, 5, 2, 11, 10, 15, 6, 4]
print(len(numbers))     # 8
