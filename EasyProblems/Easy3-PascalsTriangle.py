'''
Question
Easy 3

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''
#code ->

def generate(numRows):
    List = [] 
    list_0 = [1]
    list_1 = [1, 1]
    List.append(list_0)
    List.append(list_1)

    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    if numRows >= 3:
        for i in range(2, numRows): 
            list_i = [1] 
            for j in range(1, i):
                list_i.append(List[i - 1][j - 1] + List[i - 1][j])
            list_i.append(1)
            List.append(list_i)

    return List

result = generate(5)
print(result)
    
'''
 TRACING:
    
 First i will take an empty list as List=[].
 I am initialising the first two rows manually because i know in pascals triangle the root node and the outer side nodes are 1.
 list_0 = [1]
 list_1 = [1, 1]
 Append list_0 to List: List = [[1]]
 Append list_1 to List: List = [[1], [1, 1]]
    
 Check if numRows is 1 or 2. Since numRows is 5, i proceeded to the next step.

 Enter a loop for generating additional rows starting from the third row (i = 2):

 Iteration 1 (i = 2):

 Initialize list_i = [1]
 Enter a nested loop from j = 1 to i - 1 (j = 1):
 Calculate list_i[1] = List[1][0] + List[1][1] = 1 + 1 = 2
 Append 1 to list_i: list_i = [1, 2, 1]
 Append list_i to List: List = [[1], [1, 1], [1, 2, 1]]
 Iteration 2 (i = 3):

 Initialize list_i = [1]
 Nested loop (j = 1):
 Calculate list_i[1] = List[2][0] + List[2][1] = 1 + 2 = 3
 Nested loop (j = 2):
 Calculate list_i[2] = List[2][1] + List[2][2] = 2 + 1 = 3
 Append 1 to list_i: list_i = [1, 3, 3, 1]
 Append list_i to List: List = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
 Iteration 3 (i = 4):

 Initialize list_i = [1]
 Nested loop (j = 1):
 Calculate list_i[1] = List[3][0] + List[3][1] = 1 + 3 = 4
 Nested loop (j = 2):
 Calculate list_i[2] = List[3][1] + List[3][2] = 3 + 3 = 6
 Nested loop (j = 3):
 Calculate list_i[3] = List[3][2] + List[3][3] = 3 + 1 = 4
 Append 1 to list_i: list_i = [1, 4, 6, 4, 1]
 Append list_i to List: List = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
 Iteration 4 (i = 5): (This is the last iteration since numRows = 5)

 Initialize list_i = [1]
 Nested loop (j = 1):
 Calculate list_i[1] = List[4][0] + List[4][1] = 1 + 4 = 5
 Nested loop (j = 2):
 Calculate list_i[2] = List[4][1] + List[4][2] = 4 + 6 = 10
 Nested loop (j = 3):
 Calculate list_i[3] = List[4][2] + List[4][3] = 6 + 4 = 10
 Nested loop (j = 4):
 Calculating list_i[4] = List[4][3] + List[4][4] = 4 + 1 = 5
 Append 1 to list_i: list_i = [1, 5, 10, 10, 5, 1]
 Append list_i to List: List = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
 Return the final result: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    
'''
