balance = 3329
annualInterestRate = 0.2
mpay = 0
while True:
	mpay += 10
	b = balance
	r = annualInterestRate
	for i in range(0,12):
		b = b - mpay
		b = b + ((r /12) * b)
	if b <= 0:
		break
print("Lowest Payment: " + str(mpay))
