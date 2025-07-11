# numbers = [1, 2, 3, 4, 5]
# numbers[4] = 6
# print(numbers[4])

# list1 = [1, 2, 3, 4, 5]
# list1[0] = 10
# print(list1)

# list1 = [10, 11, 12, 13, 14]
# print(list1[::3])

# list1=['UK','India','Canada']

# list1.insert(1,8)

# print(list1)

# ages = [56, 72, 24, 46]
# ages.sort()
# print(ages)

# list1 = [4, 4, 3, 1]
# list1.pop(2)
# print(list1)

# list1 = [10, 20, 30, 40, 50]
# list1.append(60)
# print(list1)

# list1=["Go","Java","C","Python"]
# print(max(list1))

# list1=["Go","Java","C","Rust"]
# print(min(list1))

# for x in [0, 1, 1, 3]:
#     for y in [0, 2, 1, 2]:
#             print('*')

# for x in [0, 2, 1, 3]:
#     for y in [0, 4, 1, 2]:
#             print('*')

# # Define the lists
# x_values = [0, 2, 1]
# y_values = [0, 4, 1]

# # Loop through the lists and print asterisks
# for x in x_values:
#     for y in y_values:
#         print('*')

# # Calculate the total number of asterisks
# total_asterisks = len(x_values) * len(y_values)

# # Print the result dynamically
# print(f"The code will print {total_asterisks} asterisks in total.")

# for letter in 'KodeKloud':
#     if letter == 'e':
#         continue
#     print('Letter : ' + letter)

# sum = 0
# values = [2,9,1,7]
# for number in values:
#     sum = sum + number

# print(sum)

# sum = 0
# values = [2,9,1,7]
# for number in values:
#     sum += number

# print(sum)

# list1=[4,0,7,1]
# print(list1[::-1])

# letters = ["A", "B", "C", "D", "E"]
# print(letters[1:])

# list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10],[1,2,3,4],[4,5,6,7,8,9]]
# for i in list1:
#       if len(i)==4:
#         print(i)


# list1 = [10, 11, 12, 13, 14]
# print(list1[::1])

# list1 = [1, 2, 3, 4]
# for i, j in enumerate(list1):
#      print(i, j)

# list1 = [1, 2, 3, 4]
# for index, j in enumerate(list1):
#      print(index, j)

# list1=["usa","canada","india"]
# list1=[]
# list1=[]*2

# my_list = [0, 1, 2, 3, 4]
# print(my_list[2:4])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[::3])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[:2])

# my_list = [0, 1, 2, 3, 4]
# my_list.append("python")
# print(my_list[2:])

# list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
# print(list1[0:4])

# my_list = [0, 1, 2, 3, 4]
# my_list.append("python")
# b = my_list[1:]
# print(b)

# my_list = [0, 1, 2, 3, 4]
# print(my_list[::-1])

# my_list = [0, 1, 2, 3, 4]
# print(my_list[-1])

# countries = ["USA", "Canada", "India"]
# countries[0], countries[1] = countries[1], countries[0]
# print(countries)

# list1 = [0, 3, 4, 1, 2]
# list1[1]=[8,9]
# print(list1)

# print((4, 6) not in [(4, 7), (5, 6), "hello"])

# list1 = [0, 3, 4, 1, 2, 3, 5, 6, 3]
# list1[2:5]=[8,9]
# print(list1)

# list1 = [0, 3, 4, 1, 2]
# list1[2:4]=[1,2]
# print(list1)

# matrix = [[j for j in range(4)] for i in range(4)] 
# # print(matrix[1][2])
# print(matrix)

# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2])


# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)

# print(a)

# countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
# print(countries2)


# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)

# print(matrix2[2][0])