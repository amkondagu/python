import random
secret = str(random.randint(1000,9999))

while True:
	pastPositions = []
	pastPositions2 = []
	guess = None

	while True:
		try:
			guess = int(input("guess a four digit number : "))

			if len(str(guess)) == 4:
				break
			else:
				print("invalid input")

		except:
			print('invalid input')

	cows = 0
	bulls = 0

	for position in range(4):
		for position2 in range(4):
			if str(guess)[position] == secret[position]:
				bulls += 1
				pastPositions.append(position)
				pastPositions2.append(position)
				break
	for position in range(4):
		for position2 in range(4):
			if str(guess)[position] == secret[position2]:
				if (position2 not in pastPositions2) and (
				    position not in pastPositions):
					cows += 1
					pastPositions2.append(position2)
					pastPositions.append(position)
				
	if bulls == 4:
		print("you win!")
		print("the number was", secret)
		break
		
	print(bulls, "bull(s)")
	print(cows, "cow(s)")
