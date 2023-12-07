'''
Question:
Hard 3

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Example 1:
Input: n = 13
Output: 6

'''
#code ->

class Solution(object):
    def countDigitOne(self, n):
        count = 0
        factor = 1

        while factor <= n:
            Divisor = factor * 10
            full_repetitions = (n // Divisor) * factor
            remaining_part = max(n % Divisor - factor + 1, 0)
            partial_occurrences = min(remaining_part, factor)
            count = count + full_repetitions + partial_occurrences
            factor = factor * 10

        return count

'''
TRACING:
At first i'm initialising count=0 and factor=1 
Iteration 1
This is for the 1's in one's place digit .
Divisor = factor * 10 = 1*10 = 10
full_repetitions = (13 // 10) * 1 = 1 * 1 = 1
remaining_part = max(13 % 10 - 1 + 1, 0) = max(3, 0) = 3
partial_occurrences = min(3, 1) = 1
count = count + full_repetitions + partial_occurrences = 0 + 1 + 1 = 2
factor = factor * 10 = 10

Iteration 2
This is for the 1's in ten's place.
Divisor = factor * 10 = 100
full_repetitions = (13 // 100) * 10 = 0 * 10 = 0
remaining_part = max(13 % 100 - 10 + 1, 0) = max(13 - 10 + 1, 0) = 4
partial_occurrences = min(4, 10) = 4
count = count + full_repetitions + partial_occurrences = 2 + 0 + 4 = 6
factor = factor * 10 = 100
now the loop terminates because the while loop conditioned factor<n fails
Total count= 2(one's place)+4(ten's place)=6

'''