#!/bin/python3

import sys
results = {}
def tileStackingProblem(n, m, k):
    if n==0:
        return 1
    elif (m == 0) | (n > m*k):
        return 0

    sum = 0;
    tup = (n,m,k)
    if tup in results:
        return results[tup]

    for i in range(0,k+1):
        tup = (n-i,m-1,min(k,n-i))
        if tup in results :
            subsum =  results[tup]
        else:
            subsum = tileStackingProblem(n-i,m-1,min(k,n-i))
            results[tup] = subsum
        sum += subsum


    return sum%1000000007

    # Complete this function

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]

    result = tileStackingProblem(n, m, min(n,k))
    print(result)