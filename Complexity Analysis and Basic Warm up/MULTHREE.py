'''
Consider a very long K-digit number N with digits d0, d1, ..., dK-1 (in decimal notation; d0 is the most significant and dK-1 the least significant digit). This number is so large that we can't give it to you on the input explicitly; instead, you are only given its starting digits and a way to construct the remainder of the number.

Specifically, you are given d0 and d1; for each i ≥ 2, di is the sum of all preceding (more significant) digits, modulo 10 — more formally, the following formula must hold: 

di = summation(dj)mod10, 2<=i<k
        j->0to i-1

Determine if N is a multiple of 3.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains three space-separated integers K, d0 and d1.
Output
For each test case, print a single line containing the string "YES" (without quotes) if the number N is a multiple of 3 or "NO" (without quotes) otherwise.

Constraints
1 ≤ T ≤ 1000
2 ≤ K ≤ 1012
1 ≤ d0 ≤ 9
0 ≤ d1 ≤ 9
Example
Input:
3
5 3 4
13 8 1
760399384224 5 1

Output:
NO
YES
YES
Explanation
Example case 1: The whole number N is 34748, which is not divisible by 3, so the answer is NO.

Example case 2: The whole number N is 8198624862486, which is divisible by 3, so the answer is YES.
'''
# cook your dish here
testcases = int(input())
for i in range(testcases):
    k,d0,d1 = input().split();
    k = int(k)
    #d0,d1,d2 will vary
    d0 = int(d0)
    d1 = int(d1)
    s = d0+d1
    total = 0
    if k==2:
        total = s
    else:
        #cycle begins from d3
        c = ((s*2)%10)+((s*4)%10)+((s*8)%10)+((s*6)%10)
        num_cycles = (k-3)//4
        sum_of_cycles = num_cycles*c
        total = s+(s%10)+sum_of_cycles
        num_of_leftover = (k-3)-(num_cycles*4)
        p = 2
        #Finding sum of leftover values
        for i in range(1,num_of_leftover+1):
            total = total+(p*(s%10))%10
            p = (2*p)%10
    if total%3==0:
        print("YES")
    else:
        print("NO")