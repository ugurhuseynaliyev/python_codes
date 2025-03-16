def age_group(age):
    if age > 0 and age <= 12:
        return 'Child'
    elif age >= 13 and age <= 19:
        return 'Teenager'
    elif age >= 20 and age <= 64:
        return 'Adult'
    else:
        return 'Senior'

age = int(input('Enter your age: '))
print(age_group(age))