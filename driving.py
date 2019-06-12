country = input('what is your country? ')
age = input('how old are you? ')
age = int(age)
if country == 'Taiwan':
    if age >= 18:
        print('you can have a driving test')
    else:
        print('you can not have a driving test')
elif country == 'Japan':
    if age >= 18:
        print('you can have a driving test')
    else:
        print('you can not have a driving test')
elif country == 'USA':
    if age >= 16:
        print('you can have a driving test')
    else:
        print('you can not have a driving test')
else:
    print('this program is only for Taiwan, Japan, and USA')