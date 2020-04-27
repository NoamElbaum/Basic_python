def hobbies(name, age, hobby, *optional_hobbies, **others):
    int(age)
    return f'my name is {name}, my age is {age}.\nI like to {hobby}{optional_hobbies}.{others}'


cname=input('enter a name: ')

if cname == 'noam':
    print(hobbies('noam', 19, 'python', 'electronics', collage='hermelin'))
