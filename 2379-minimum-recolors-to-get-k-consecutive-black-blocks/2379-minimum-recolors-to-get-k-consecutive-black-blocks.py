class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        total = blocks[0:k]
        curr = 0
        
        for i in total:
            if i == "W":
                curr += 1
        count = curr
        l = 0
        for r in range(k,len(blocks)):
            if blocks[r] == "W":
                curr += 1
            if blocks[l] == "W":
                curr -= 1
            l += 1
            count = min(curr,count)
        return count
            
            
            
            
        
            
        