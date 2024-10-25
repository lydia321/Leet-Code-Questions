class TireNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Tire:
    def __init__(self):
        self.root = TireNode()
        
    def insert(self, word):
        curr = self.root
        ans = ''
        
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                curr.children[c] = TireNode()
            ans += c
            curr = curr.children[c]
            if curr.end == True and word[i+1] == "/":
                return ans
            
        curr.end = True
        return ans
            
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Tire()
        res = []
        folder.sort()
        for f in folder:
            
            val = root.insert(f)
            if val not in res:
                res.append(val)
        return res            
        
            
        