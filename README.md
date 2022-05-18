# NP-Complete-Partition
## Description:
 <br>The "partition problem", or number partitioning, is the task of deciding whether a given multiset S of positive integers can be partitioned into two subsets S1 and S2 such that the sum of the numbers in S1 equals the sum of the numbers in S2.
 <br>__Example__: Given S = {3,1,1,2,2,1}, a valid solution to the partition problem is the two sets S1 = {1,1,1,2} and S2 = {2,3}. Both sets sum to 5, and they partition S. Note that this solution is not unique. S1 = {3,1,1} and S2 = {2,2,1} is another solution.
## Proof why it is in NP class:
<br>Set Partition Problem is in NP:
If any problem is in NP, then, given a ‘certificate’, which is a solution to the problem and an instance of the problem (a set S and two partitions A and A’, in this case), it can be proved that the certificate in polynomial time. This can be done in the following way:  
* For every element x in A and x’ in A’, verify that all the elements belonging to S are covered.
* Let S1 is 0, S2 is 0
* For every element x in A add that value to S1.
* For every element x’ in A’ add that value to S2.
* Verify that S1 is the same as S2.
## Problem:
Given a set of integer numbers, return __true__ if the set can be partitioned into two sets with equal sum, if not then return __false__
## How to solve:
### Brute force:
* A basic brute-force solution could be to try all combinations of partitioning the given numbers into two sets to see if any pair of sets has an equal sum.
* Assume if S represents the total sum of all the given numbers, then the two equal subsets must have a sum equal to S/2. This essentially transforms our problem to: "Find a subset of the given numbers that has a total sum of S/2". If the sum S is odd then we need to return false.
```
for each number 'num' 
  create a new set which INCLUDES number 'num' if the sum does not exceed 'S/2', and recursively 
      process the remaining numbers
  create a new set WITHOUT number 'num', and recursively process the remaining items 
return true if any of the above sets has a sum equal to 'S/2', otherwise return false
```
### Top-down Dynamic Programming with Memoization:
<br>We can use memoization to reduce the overlapping sub-problems. Memoization is when we store the results of all the previously solved sub-problems return the results from memory if we encounter a problem that has already been solved.
<br>Since we need to store the results for every subset and for every possible sum, therefore we will be using a two-dimensional array to store the results of the solved sub-problems. The first dimension of the array will represent different subsets and the second dimension will represent different ‘sums’ that we can calculate from each subset.
### Bottom-up Dynamic Programming:
```
So, for each number at index ‘i’ (0 <= i < num.length) and sum ‘s’ (0 <= s <= S/2), we have two options:

  Exclude the number. In this case, we will see if we can get ‘s’ from the subset excluding this number: dp[i-1][s]
  Include the number if its value is not more than ‘s’. In this case, we will see if we can find a subset to get the remaining sum: dp[i-1][s-num[i]]
If either of the two above scenarios is true, we can find a subset of numbers with a sum equal to ‘s’.
```
## Time Complexity:
### Bruteforce:
The time complexity of the brute force is exponential `O(2^n)`., where ‘n’ represents the total number. The space complexity is `O(n)`
### Top-down Dynamic Programming with Memoization:
<br>Although the partition problem is NP-complete, there is only __a pseudo-polynomial time__ dynamic programming solution, and there are heuristics that solve the problem in many instances, either optimally or approximately. For this reason, it has been called "the easiest hard problem". It is not exact polymomial time, but it is optimal when the value of numbers are not very large.

<br>The above algorithm has time and space complexity of `O(N*S)`, where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
### Bottom-up Dynamic Programming:
<br>The above algorithm has time and space complexity of `O(N*S)`, where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.

