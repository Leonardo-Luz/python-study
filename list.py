numbers = [1 , 10 , 100 , 1000 , 10000]
animals = ['parrot', 'chicken', 'dog', 'bettle']

mix = [numbers, animals]

# NOTE: Basic array behavior
print(numbers[0])
print(numbers[3])

# NOTE: 1:4 returns a new sliced list between 1 and 4, 1 is included while 4 isnt
# in the case below, the new array will be [10, 100, 1000]
print(numbers[1:4])

# NOTE: Basic matrix behavior: The first number gets which list, while the second get the element
# in the case below, the list will be 'animals' while the element will be dog
print(mix[1][2])

# NOTE: Creates a new sliced list and prints the last element of it
print(mix[1][2:3][-1])

# NOTE: Inserts new data from the beginning until 2
animals[:2] = ['bird', 'bird']
print(animals)

# NOTE: Inserts new data from 2 until the end
animals[2:] = ['mammal', 'insect']
print(animals)

# NOTE: Delete element
del numbers[2]
print(numbers)

# NOTE: Some operations

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

print('bird' in animals)
print('fish' not in animals)
print(1 not in numbers)

print(list('a new array'))

numbersRange = list(range(0, 100, 10))

print(len(numbersRange))

print(numbersRange)
numbersRange.sort(reverse=True)
print(numbersRange)
