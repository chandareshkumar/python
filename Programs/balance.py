"""All submissions for this problem are available.
Pooja would like to withdraw X $US from an ATM. 
The cash machine will only accept the transaction if X is a multiple of 5, and 
Pooja's account balance has enough cash to perform the withdrawal 
For each successful withdrawal the bank charges 0.50 $US. 
Pooja's account balance after an attempted transaction."""




withdraw= int(input("Enter the amount to withdraw"))

amount= float(input("Enter the amount to balance amount"))


if (withdraw>amount+0.50) or (withdraw%5 !=0):
	print('%.2f' % amount)

else:
	amount=amount-withdraw-0.50
	print('%.2f'% amount)	


