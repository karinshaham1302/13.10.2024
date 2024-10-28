# start

sum_negative = 0

while True:
    number: int = int(input('enter a number:'))
    if number == 0:
        break
    if number < 0:
        sum_negative += number

print('the sum of negative number is: ',sum_negative)

# stop
