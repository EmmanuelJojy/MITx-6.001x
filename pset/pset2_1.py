balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(0,12):
	balance = balance - (balance * monthlyPaymentRate)
	balance = balance + ((annualInterestRate /12) * balance)
balance = round(balance, 2)
print("Remaining balance: " + str(balance))
