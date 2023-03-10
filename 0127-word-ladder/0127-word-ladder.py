class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList :
            return 0
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        print(graph)
        visited = set([beginWord])
        queue = [beginWord]
        res = 1
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    
                    for j in graph[pattern]:
                        if j not in visited:
                            visited.add(j)
                            queue.append(j)
            res += 1
        return 0
                    
        
        