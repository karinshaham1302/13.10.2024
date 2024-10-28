# start

prime_count = []

while True:
    number = int(input('enter a number:'))
    if number == 0:
        break
    if number < 0:
        print('must be equal or larger than 1')
    else:
        if number == 1:
            print(f'{number} is not prime')
        else:
            divider: int = 3
            found_divider: bool = False
            while divider <= number ** 0.5 + 1:
                if number % divider == 0:
                    found_divider: bool == True
                    break
                divider += 2
            if not found_divider:
                prime_count.append(number)

print('count of prime numbers:', prime_count)

# stop
