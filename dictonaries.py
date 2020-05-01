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
print("Coordinates for yellow alien are: " + str(alien_0['position_x']) + ", " +
      str(alien_0['position_y']))

''' Adding new features to my alien_0'''
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['position_x'] = alien_0['position_x'] + x_increment

print("New value of position x for medium speed alien is: " + str(alien_0['position_x']))
print("That mean the new coordinates are: " + str(alien_0['position_x']) + ", " +
      str(alien_0['position_y']))