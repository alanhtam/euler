# A palindromic number reads the same both ways. The largest palindrome made
# from a product of 2-digit numbers is 9009 = 91 X 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def max_palindrome():
	n = 0
	for a in xrange(999,100,-1):
		for b in xrange(a,100,-1):
			c = a*b
			if str(c)==str(c)[::-1] and c>n: n=c
	print n
