cowboy = {'age': 32, 'horse':'mustang', 'hat_size': 'large'}

if 'age' in cowboy:
    age = cowboy['age']
else:
    age = 'no age'
print(age)

#for a in cowboy:
if 'name'not in cowboy:
    name = 'The Man with No Name'
print(name)

size = cowboy.get('height')
print(size)

if 'horse' in cowboy:
    horse = cowboy['horse']
else:
    horse = 'The Man with No horse value'
print(horse)

    
