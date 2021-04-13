states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California':'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has:', cities['OR'])

# Print some states
print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# Every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

# Default Value
city = cities.get('TX', 'Does Not Exist')
print(f'The city for the state of "TX" is: {city}')