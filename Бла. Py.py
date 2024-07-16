favorite_languages = { 
    'Phil': 'phyton', 
    'Ben': 'C++',
    'Jack': 'phyton',
    'Mike': 'Go', 
    'Edward': 'ruby', 
    }
    
print('Список всех участников: \n')
for man in favorite_languages:
    print (man)

name = input('\nВведите имя\n')

print(favorite_languages[name])
