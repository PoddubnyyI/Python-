#Списки

names = []
names.insert(0, input('Кто сказал?\n'))
names.insert(1, input('Кому сказал?\n'))
names.insert(2, input('А третий кто?\n'))

m = f"{names[0].title()} сказала {names[1].title()} купить молока, потому что {names[2].title()} хочет кофе"
print(m)


