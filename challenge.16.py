# start

num: int = int(input('enter a number:'))
save: int = num
sum_digit: int = 0
print(num, ':', end=' ')

while num > 0:
    ahadot: int = num % 10
    sum_digit += ahadot
    num = num // 10
    print(f'{ahadot}{' + ' if num > 0 else ' '}', end=' ')
print('=', sum_digit)

print('the sum is divided by 3' if sum_digit % 3 == 0 else 'the sum is NOT divided by 3')

# stop
