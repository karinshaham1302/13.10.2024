# start

number1: int = int(input('enter the first number:'))
number2: int = int(input('enter the second number:'))

print([i for i in range(number1, number2 + 1) if i % 2 == 0])

# stop
