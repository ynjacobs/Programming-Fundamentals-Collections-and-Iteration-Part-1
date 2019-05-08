from exercise0 import*

print(sum(cities_dictionary.values()))


for key, val in names_ages_dictionary.items():
    if val < 12:
        print('{} is a child'.format(key))
    elif val > 12:
        print('{} is a teen'.format(key))

print(fav_colours[1:3])

ages = [x + 1 for x in ages]
print(ages)

fav_colours.append('yellow')
fav_colours.append('green')
print(fav_colours)