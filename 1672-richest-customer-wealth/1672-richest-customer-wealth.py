class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s = float(-inf)
        
        for account in accounts:
            s = max(s, sum(account))    
            
        return s
       