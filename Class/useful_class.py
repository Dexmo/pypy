""" File with fine class - OrderedDict from collections"""
from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['john'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['paul'] = 'python'

for name, language in favorite_language.items():
    print("Favorite language of user " + name.title() + " is " +
          language.title() + ".")

# As you can see order of key-value pairs are same when we show them.
