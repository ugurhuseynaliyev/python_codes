value = input('Type something: ')
if value == '':
    value = None
    print('No input provided')
else:
    print(value, type(value))
