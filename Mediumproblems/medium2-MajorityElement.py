'''
Question: Medium 2
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 Example 1:
Input: nums = [3,2,3]
Output: [3]

'''
'''
ALGORITHM:
By using the Extended Boyer Moore’s Voting Algorithm,
This algorithm aims to find two potential majority elements (el1 and el2) in an array because for a number 'n' at max only 'n-1' elements could be present.
while iterating through the array 
1)If cnt1 is 0 and the current element is not el2, it updates el1 and increments cnt1.
2)If cnt2 is 0 and the current element is not el1, it updates el2 and increments cnt2.
3)If the current element matches el1 or el2, the respective count is increased or else both are decremented.
 At the end the algorithm manually checks the counts of el1 and el2 and any element with a count greater than the floor(N/3), if yes then it is the majority element.

'''
#code:

from typing import List

def majorityElement(nums: List[int]) -> List[int]:
    n = len(nums) # size of the array

    cnt1, cnt2 = 0, 0 # counts
    el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

    # applying the Extended Boyer Moore’s Voting Algorithm:
    for i in range(n):
        if cnt1 == 0 and el2 != nums[i]:
            cnt1 = 1
            el1 = nums[i]
        elif cnt2 == 0 and el1 != nums[i]:
            cnt2 = 1
            el2 = nums[i]
        elif nums[i] == el1:
            cnt1 += 1
        elif nums[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = [] # list of answers

    # Manually checking if the stored elements in el1 and el2 are majority or not
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if nums[i] == el1:
            cnt1 += 1
        if nums[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)
    return ls

arr = [3,2,3]
ans = majorityElement(arr)
print( end="")
for it in ans:
    print(it, end=" ")
print()

'''
TRACING:
considering arr=[3,2,3]
n=3 
initialise cont1 and cnt2 to 0
initialise el1 and el2 to negative infinity
Looping through the array,
For the first element (3), cnt1 is 0, so set cnt1 to 1 and el1 to 3.
For the second element (2), cnt2 is 0, so set cnt2 to 1 and el2 to 2.
For the third element (3), el1 is equal to the current element, so increment cnt1.
After this loop, el1 is 3 and el2 is 2.
Manually checking if el1 and el2 are majority elements by counting their occurrences in the original array.
For element 3, cnt1 is 2, which is greater than mini, so append 3 to ls.
For element 2, cnt2 is 1, which is not greater than mini.
The majority element is 3.


'''