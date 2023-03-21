class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class WordDictionary:
    def __init__(self):
        self.dict = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.dict
        
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True
    
    def search(self, word: str) -> bool:
        curr = self.dict
        
        def dfs(idx,curr_root):
            
            for i in range(idx,len(word)):
                if word[i] == '.':
                    for val in curr_root.children.values():
                        if dfs(i + 1,val):
                            return True
                    return False
                else:
                    if word[i] not in curr_root.children:
                        return False
                    curr_root = curr_root.children[word[i]]
            return curr_root.end
        
        return dfs(0,curr)
        
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)