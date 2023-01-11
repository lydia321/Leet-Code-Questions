class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.range = []
        
        for i in range(len(rects)):
            num_points = (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)
            self.range.append(num_points)

    def pick(self) -> List[int]:
        #returns a list with the randomly selected element from the specified sequence
        rect = random.choices(self.rects,self.range)[0] 
        #returns an integer number selected element from the specified range. 
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3]) 

        return [x,y]
# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()