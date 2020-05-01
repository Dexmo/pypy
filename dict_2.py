#New dictionary - trying to use as contact book

user_0 = {
    'user_name': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Wartość: " + value)

print(user_0.keys())
print(user_0.values())

# Dictioneries in dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie':{
        'first': 'maria',
        'last': 'skłodowska-curie',
        'location': 'paryż',
    },
}

for username, user_info in users.items():
    print("\nUser name: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\t Name and surname: " + full_name.title())
    print("\t Location: " + location.title())