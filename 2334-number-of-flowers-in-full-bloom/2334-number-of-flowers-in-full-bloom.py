class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
            
        n = len(people)
        m = len(flowers)
        
        flowers.sort()
        
        que = [[val, ind] for ind, val in enumerate(people)]      
        que.sort()
           
        hp = []
        heapify(hp)
        
        ans = [-1]*n
        
        i = 0
   
        for val, ind in que:
            while i < m and val >= flowers[i][0]:
                s, e = flowers[i] 
                heappush(hp, e)
                i += 1
                
            while hp and hp[0] < val:
                heappop(hp)

            ans[ind] = len(hp)
            
        return ans