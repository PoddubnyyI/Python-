age = int(input('Введите ваш возраст \n'))

if age < 12:
    print('Ну ты малой')
if  12 > age < 18:
    print('Ну ты молодой')
elif 18 > age < 30:
    print('Ну ты средняк')
elif 30 > age < 50:
    print('Ну ты повидавший')
elif 50 > age < 70:
    print('Ну ты дед')
else:
    print('Ну ты совсем дед')
