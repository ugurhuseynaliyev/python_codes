password = input('Enter password: ')
hasUpper = False
hasLower = False
hasDigit = False

for char in password:
    if char.isupper():
        hasUpper = True
    if char.islower():
        hasLower = True
    if char.isdigit():
        hasDigit = True

if len(password) >= 8 and hasUpper and hasLower and hasDigit:
    print('Strong')
elif len(password) < 8:
    print('Length of password must be at least 8 characters')
elif not(hasUpper) or not(hasLower) or not(hasDigit):
    print('Password must contain uppercase, lowercase and digits')
else:
    print('Weak')