#!/usr/bin/env python

from collections import defaultdict
import numpy as np
import bisect

#algo1-programming_prob-2sum 
def _read_numbers(file_name='algo1-programming_prob-2sum.txt'):
	numbers = []
   
	for line in open(file_name,'r'):
		line = line.strip()
		numbers.append(int(line))
	return numbers
	
def find_ge(a, x, upper_bound):
    'Find index of leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] < upper_bound:
        return i
    else:
		return -1
		
def find_le(a, x, lower_bound):
	'Find rightmost index of item less than or equal to x'
	i = bisect.bisect_right(a, x)
	if i and a[i-1] > lower_bound:
		return i-1
	else:
		return -1
	
def twosum_counter(sorted_numbers):
	two_sum_pairs = set()
	t_values = set()
	
	for number in sorted_numbers:
		lower_bound_y = -10000 - number
		upper_bound_y = 10000 - number
		#find index in sorted_numbers of a number equal to or greater than lower_bound_y (and lower than upper_bound_y)
		lower_bound_index = find_ge(sorted_numbers, lower_bound_y, upper_bound_y)
		#find index in sorted_numbers of a number equal to or less than upper_bound_y (and greater than lower_bound_y)
		upper_bound_index = find_le(sorted_numbers, upper_bound_y, lower_bound_y)
	
		if lower_bound_index == -1 and upper_bound_index != -1:
			if number != sorted_numbers[upper_bound_index] and (sorted_numbers[upper_bound_index],number) not in two_sum_pairs:
				pair = (number,sorted_numbers[upper_bound_index])
				two_sum_pairs.add(pair)
				t_values.add(number+sorted_numbers[upper_bound_index])
		elif upper_bound_index == -1 and lower_bound_index != -1:
			if number != sorted_numbers[lower_bound_index] and (sorted_numbers[lower_bound_index],number) not in two_sum_pairs:
				pair = (number,sorted_numbers[lower_bound_index])
				two_sum_pairs.add(pair)
				t_values.add(number+sorted_numbers[lower_bound_index])
		elif upper_bound_index != -1 and lower_bound_index != -1:
			# a lower bound and upper bound index were found in the sorted numbers
			# go through sorted numbers from lower bound index to upper bound index, add the number at the index to the set of 
			# two-sum numbers that add to give a sum in the range -10000 to 10000
			for y_index in range(lower_bound_index, upper_bound_index + 1):
				if number != sorted_numbers[y_index] and (sorted_numbers[y_index],number) not in two_sum_pairs:
					pair = (number,sorted_numbers[y_index])
					two_sum_pairs.add(pair)
					t_values.add(number+sorted_numbers[y_index])
				
	return two_sum_pairs, t_values			
	
if __name__ == '__main__':
	numbers = _read_numbers()
	numbers.sort()
	#print numbers
	print len(numbers)," numbers read into list"
	sorted_numbers = numbers
	two_sum_pairs, t_values = twosum_counter(numbers)
	print len(two_sum_pairs)," two sum pairs in list that sum within range -10000 to 10000"
	print len(t_values)," t values between -10000 to 10000 for list of numbers"
	#print two_sum_pairs
	