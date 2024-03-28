list = [1, 2, 3, 4, 5]


print("Original list:",list)
temp =list[0]
list[0] = list[-1]
list[-1] = temp
print("List after interchanging first and last elements:",list)