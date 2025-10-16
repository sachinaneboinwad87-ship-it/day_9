# Create a List:
# fruits = ["apple", "banana", "cherry"]
# print(fruits)


# Lists allow duplicate values:
# fruits = ["apple", "banana", "cherry", "apple", "cherry"]
# print(fruits)

# A list can contain different data types:
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# Print the second item of the list:
# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])

# Print the last item of the list:
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

# list method#
# Create a list
# fruits = ["apple", "banana", "cherry"]
# print("Original list:", fruits)

# 1. append() - Add an item to the end of the list
# fruits.append("orange")
# print("After append:", fruits)

# 2. insert() - Add an item at a specific position
# fruits.insert(1, "mango")
# print("After insert:", fruits)

# 3. remove() - Remove the first occurrence of a value
# fruits.remove("banana")
# print("After remove:", fruits)

# 4. pop() - Remove an item at a specific index (or last if not specified)
# popped_item = fruits.pop(2)
# print("Popped item:", popped_item)
# print("After pop:", fruits)

# 5. index() - Find the index of an element
# index_cherry = fruits.index("cherry")
# print("Index of 'cherry':", index_cherry)

# 6. count() - Count how many times an item appears
# fruits.append("apple")
# count_apple = fruits.count("apple")
# print("Count of 'apple':", count_apple)

# 7. sort() - Sort the list in ascending order
#fruits.sort()
# print("After sort:", fruits)

# 8. reverse() - Reverse the order of the list
# fruits.reverse()
# print("After reverse:", fruits)

#  9. copy() - Create a shallow copy of the list
# copy_list = fruits.copy()
# print("Copied list:", copy_list)

#  10. clear() - Remove all elements from the list
# fruits.clear()
# print("After clear:", fruits)



# list comprehension
# numbers = [1, 2, 3, 4, 5]
# squares = [n**2 for n in numbers]
# print("Squares:", squares)

# With condition
# even_numbers = [n for n in numbers if n % 2 == 0]
# print("Even numbers:", even_numbers)

# Using string operations
# words = ["apple", "banana", "cherry"]
# capitalized = [word.upper() for word in words]
# print("Uppercase words:", capitalized)

# Nested list comprehension (2D list)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print("Flattened list:", flattened)

# Using if-else inside comprehension
# labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
# print("Even/Odd labels:", labels)
