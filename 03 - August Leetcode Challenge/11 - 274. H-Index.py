"""
274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        bucket = [0 for x in range(n+1)] 

        for i in range(n):
            bucket[min(citations[i],n)]+=1

        total_papers = 0
        temp=0
        p=len(bucket)

        for i in range(p-1,-1,-1):
            total_papers=total_papers+bucket[i]
            print(total_papers," ",i,"kk")
            if(total_papers >=i):
                temp=i
                break

        return temp