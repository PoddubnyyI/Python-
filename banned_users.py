# Программа для проверки гостей на предмет бана и возраста.
# есть возможность добавлять в черный список людей, но этот список живет только пока работает программа


banned_users = ['Jack', 'Emma', 'Nik', 'Mike']
user = input('Введите имя: \n')
age = int(input('Введите возраст: \n'))

# print(banned_users)

if user in  banned_users  and age >= 18:
    print(f"{user.title()}, Вы в списке приглашенных.")

elif age < 18:
    print(f"{user.title()},Вы не проходите по возрасту")

else:
    print(f"{user.title()},Вас не приглашали...")


print('Если Вы хотите добавть гостя в черный список, то напишите его имя')

banned_users.append(input())

print(banned_users)
