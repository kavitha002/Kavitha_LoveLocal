/*
Question 
Hard 2
You are given a string s. You can convert s to a 
palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
*/

/*
Algorithm:
 By using the Knuth–Morris–Pratt (KMP) algorithm which is a string-searching algorithm.
Longest prefix(right to left) suffix (left to right) method.
firstly, searching for the longest substring starting from the 0th index.
secondly,reversing the remaining substring and adding it at the beginning. 
*/

//code ->
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void func(vector<int>& lps, string a) {
        int i = 0, j = 1;

        while (j < a.length()) {
            if (a[i] == a[j]) {
                i++;
                lps[j] = i;
                j++;
            } else {
                if (i == 0) {
                    j++;
                } else {
                    i = lps[i - 1];
                }
            }
        }
    }

    string shortestPalindrome(string s) {
        string t = s;
        reverse(t.begin(), t.end());
        string a = s + '#' + t;
        vector<int> lps(a.length(), 0);

        func(lps, a);

        int i = lps[a.length() - 1];
        string temp = s.substr(i);
        reverse(temp.begin(), temp.end());

        return temp + s;
    }
};

int main() {
    Solution solution;

    // Example usage
    string input_str = "abcd";
    string output_str = solution.shortestPalindrome(input_str);

    cout << "Input: " << input_str << endl;
    cout << "Output: " << output_str << endl;

    return 0;
}

/*
Tracing:

Initialization:
input_str = "abcd"

shortestPalindrome Function:
t = "abcd" (reverse of s)
a = "abcd#dcba"
lps array is initialized with zeros: [0, 0, 0, ..., 0]
func Function (Building LPS Array):

i = 0, j = 1

Iteration 1:
a[0] = 'a', a[1] = 'b'
Since characters are not the same:
i remains 0
j is incremented to 2

Iteration 2:
a[0] = 'a', a[2] = 'c'
Since characters are not the same:
i remains 0
j is incremented to 3

Iteration 3:
a[0] = 'a', a[3] = 'd'
Since characters are not the same:
i remains 0
j is incremented to 4

Iteration 4:
a[0] = 'a', a[4] = '#'
Since characters are not the same:
i remains 0
j is incremented to 5

Iteration 5:
a[0] = 'a', a[5] = '#'
Since characters are not the same:
i remains 0
j is incremented to 6

Iteration 6:
a[0] = 'a', a[6] = 'd'
Since characters are not the same:
i remains 0
j is incremented to 7

Iteration 7:
a[0] = 'a', a[7] = 'c'
Since characters are not the same:
i remains 0
j is incremented to 8

Iteration 8:
a[0] = 'a', a[8] = 'a'
Characters are the same:
Increment i to 1
Set lps[8] to 1
Increment j to 9

Remaining Iterations:
Characters are not the same, and i is updated based on the LPS array.
After LPS Array is Built:
lps = [0, 0, 0, 0, 0, 0, 0, 0, 1, ...]
Continuing in shortestPalindrome Function:
i = lps[a.length() - 1] = 1
temp = s.substr(1) = "bcd"
reverse(temp) = "dcb"
Return "dcb" + "abcd" = "dcbabcd"
main Function:
output_str = solution.shortestPalindrome(input_str) = "dcbabcd"
*/