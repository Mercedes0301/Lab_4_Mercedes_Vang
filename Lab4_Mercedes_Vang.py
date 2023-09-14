upper_bound = int(input("Enter the upper bound for a check: "))

divisors_sum = 0
for num in range(1, 50):
	if num % 2 == 0:
		divisors_sum += 1
		
deficient_count = 0
perfect_count = 0
abundant_count = 0

for num in range(1, upper_bound + 2):
	
	if divisors_sum <= num:
		deficient_count += 1
	elif divisors_sum == num:
		perfect_count += 1
	elif divisors_sum > num:
		abundant_count += 1

print("Between 1 and", upper_bound, "there are: ")
print("Deficient numbers: ", deficient_count)
print("Pefect numbers: ", perfect_count)
print("Abudant numbers: ", abundant_count)
