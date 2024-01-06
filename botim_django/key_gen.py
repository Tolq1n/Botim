import random

def memorable_key(length):
    characters = 'abc0123defghijk789lmnopq4567rstuvwyz0123456789'
    key = ''.join(random.choice(characters) for _ in range(length))
    key = '-'.join([key[i:i+3] for i in range(0, len(key), 3)])
    return key

print(memorable_key(9))
