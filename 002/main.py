fib_series = [1, 2]

really_big_number = 1000000

my_sum = 0

for i in range(really_big_number):
    if i > 1:
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    if fib_series[i] > 4000000:
        break
    if fib_series[i] % 2 == 0:
        my_sum += fib_series[i]

print(my_sum)
