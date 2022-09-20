balance = 999999
annualInterestRate = 0.18
l = balance/12
u = balance + (balance * (annualInterestRate/12))
u = (u ** 12) / 12
while True:
	m = (l + u)/2
	b = balance
	r = annualInterestRate
	for i in range(0,12):
		b = b - m
		b = b + ((r /12) * b)
	if -0.05 < b < 0.05:
		break
	elif b < -0.05:
		u = m
	else: 
		l = m
print("Lowest Payment: " + str(round(m,2)))
