a = int(input())
sentence = ''
for i in range(1, a + 1):
    if i % 2 == 1:
        sentence += 'I hate'
    else:
        sentence += 'I love'

    if i != a:
        sentence += ' that '
    else:
        sentence += ' it'
print(sentence)