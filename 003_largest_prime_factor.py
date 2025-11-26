# What is the largest prime factor of the number 600851475143 ?

def find_largest_prime(num):
	counter = 2
	while counter < num:
		if num % counter == 0:
			num = num / counter
			counter = 1
		counter += 1
	return num

print(find_largest_prime(600851475143))

# 6857