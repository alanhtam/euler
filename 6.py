# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum of the first one hundred natural numbers.

def diff_sum_square(n):
	number_list = list(range(1,n+1))
	squares_list = map(lambda x: x**2, number_list)
	sum_squares = sum(squares_list)
	square_sum = sum(number_list)**2
	print square_sum - sum_squares

diff_sum_square(100)