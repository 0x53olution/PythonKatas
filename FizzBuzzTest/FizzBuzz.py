def FizzBuzzTest(max_range):
	for i in range(1, max_range):
		if i % 15 == 0:
			print(i, "FizzBuzz")
		if i % 3 == 0:
			print(i, "Fizz")
		if i % 5 == 0:
			print(i, "Buzz")

print("Start FizzBuzz Test \nInput max range of test: ")
FizzBuzzTest(int(input()))
