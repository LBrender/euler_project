# For a positive integer n, let function2(n) be the sum of the squares of its divisors
# For example, function2(10) = 1 + 4 + 25 + 100 = 130.
# Find the sum of all n, 0 < n < 64,000,000 such that function2(n) is a perfect square.

import math

def should_add(number):
	sum_of_divisors_squared = number**2 + 1
	counter = 2
	while counter * 2 <= number:
		if number % counter == 0:
			sum_of_divisors_squared += (counter**2)
		counter += 1
	return math.sqrt(sum_of_divisors_squared) % 1 == 0

counter = 1
grand_total = 0

while counter <= 64000000:
	if should_add(counter):
		grand_total += counter
	print(counter)
	counter += 1

print(grand_total)
