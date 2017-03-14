# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# if divisible by 20
def smallest_dividend(n):
	dividend = n
	divisor = 20
	while divisor > 1:
		if dividend%divisor==0:
			divisor-=1
		else:
			dividend+=20
			divisor = 20
	print dividend

smallest_dividend(2520)

	# reduce by 1 and check again
# increment base by 20 and restart
	# if divisible by 1 then end and return base

