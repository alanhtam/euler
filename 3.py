# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
	a = 2
	while n>a:
		if n%a==0:
			n = n/a
		else:
			a+=1
	print "largest prime factor: %d" % (n)

largest_prime_factor(600851475143)