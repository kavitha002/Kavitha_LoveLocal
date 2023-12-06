'''
Question: Medium 1
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 Example 1:
Input: nums = [3,2,3]
Output: [3]

'''

#method1: better approach (using a hashmap)
#code:
from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [3,2,3]
ans = majorityElement(arr)
print("The majority element is:", ans)

'''
TRACING:
considering arr=[3,2,3]
First, we create an unordered map to store the count of each element.
Now traversing through the array 
Found 3 at index 0, increase the value of key 3 in the map by 1.
Found 2 at index 1, increase the value of key 2 in the map by 1.
Found 3 at index 2, increase the value of key 3 in the map by 1.
Now, Our map will look like this:
3->2
2->1
Now traversing through the map, 
We found that the value of key 3 is greater than the floor(N/3). So, 3 is the answer.

'''

#method 2: optimal approach (using the Extended Boyer Moore’s Voting Algorithm)
#code:

from typing import List

def majorityElement(v: List[int]) -> List[int]:
    n = len(v) # size of the array

    cnt1, cnt2 = 0, 0 # counts
    el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

    # applying the Extended Boyer Moore’s Voting Algorithm:
    for i in range(n):
        if cnt1 == 0 and el2 != v[i]:
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and el1 != v[i]:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = [] # list of answers

    # Manually checking if the stored elements in
    # el1 and el2 are the majority elements:
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        if v[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)
    return ls

arr = [3,2,3]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
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