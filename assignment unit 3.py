def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

number = int(input('Enter a number: '))
if number > 0:
    countdown(number)
elif number < 0:
    countup(number)
else:
    print('Blastoff!')

