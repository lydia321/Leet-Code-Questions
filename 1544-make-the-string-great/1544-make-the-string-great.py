class Solution:
    def makeGood(self, s: str) -> str:
        arr = []
        for i in s:
            arr.append(i)
        print(arr) 
        
        output = []
        for i in range(len(arr)):
            if output:
                if arr[i] != output[-1] and arr[i].upper() == output[-1].upper():
                    output.pop()
                    continue
                output.append(arr[i])
            else:
                output.append(arr[i])
        
        return "".join(output)