''' Short program using dictionaries'''
# New dictionary
alien_0 = {'color':'green', 'points':5}

# Printing values of two elements
print(alien_0['color'])
print(alien_0['points'])

# Adding new keys and values - do not forget about '' on keys!
alien_0['position_x'] = 0
alien_0['position_y'] = 5

# Printing all dictionary
print(alien_0)

# Modify the value of key 'color'
alien_0['color'] = 'yellow'

print(alien_0)