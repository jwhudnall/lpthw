the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruid of type: {fruit}")

# Notice we have to use {} for mixed lists
for i in change:
    print(f"I got {i}")

# Example of list-building
# elements = []

# for i in range(0,6):
#     print(f"Adding {i} to the list")
#     elements.append(i)

# Alternate method:
elements = list(range(0,6))


for i in elements:
    print(f"Element was: {i}")