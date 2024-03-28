cities = {'CA': 'San Franciso','MI': 'Detroit','FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return 'Not found.'
    
cities['_find'] = find_city

while True:         # while True 是一个无限循环，直到遇到 break
    print('State? (ENTER to quit)', )
    state =input('> ')
    if not state: 
        print('Bye')
        break

    city_found = cities['_find'](cities, state)
    print(city_found)
    
