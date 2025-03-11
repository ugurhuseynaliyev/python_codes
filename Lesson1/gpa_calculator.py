def GPACalculator():
    total_point = 0
    for i in range(5):
        subject_grade = input('Enter subject grade: ')
        if subject_grade == 'A':
            subject_point = 4
        elif subject_grade == 'B':
            subject_point = 3
        elif subject_grade == 'C':
            subject_point = 2
        elif subject_grade == 'D':
            subject_point = 1
        elif subject_grade == 'F':
            subject_point = 0
        else:
            print('Invalid input!')
        total_point += subject_point
    average = total_point / 5
    if average == 4:
        print('Excellent!')
    elif average < 4 and average > 3:
        print('Good!')
    elif average <= 3 and average > 2:
        print('Need Improvement!')
    elif average <= 2:
        print('Failed!')
GPACalculator()