import statistics

# start

numbers: list[int] = []
count = 0

for _ in range(5):
    number = int(input('enter a number:'))
    numbers.append(number)
avg = statistics.mean(numbers)

for num in numbers:
    if num > avg:
        count += 1

print('average:', avg)
print('count numbers bigger than average:', count)

# stop
