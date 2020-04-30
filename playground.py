values = (1,2,3,4,5) #tuple - immutable, orderly data structure
squares = [value**2 for value in range(1,11)] #list comprehension

''' 3 short subprogram for quick work '''
print(max(values))
print(min(values))
print(sum(values))

print(squares)
'''---------------------------------------'''
for number in range(1, 21):
    print(number)

# creating list with 1000 values
thousand_list = []
for number in range(1,1001):
    thousand_list.append(number)

# creating list with odd numbers
odd_number = []
for number in range(1,20,2):
    odd_number.append(number)
print(odd_number)

# creating the list with values to cube using list comprehension
cube_values = [value**3 for value in range(1,11)]
print(cube_values)

""" taking some part of list """
players = ['Mati', 'Kati', 'Pati', "Sati"]
print(players[2:]) #Only shows Pati and Sati
print(players[:2]) #Only shows Mati and Kati

new_players = players[:]
print(new_players)