class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        l,r = 0, len(products) - 1
        
        for i in range(len(searchWord)):
            prefix = searchWord[i]
            
            while l <= r and (len(products[l]) <= i or products[l][i] != prefix):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != prefix):
                r -= 1
            curr = []
            j = l
            while len(curr) < 3 and j <= r:
                curr.append(products[j])
                j += 1
            res.append(curr)
        return res
                
        