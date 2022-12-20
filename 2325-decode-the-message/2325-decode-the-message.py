class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        lookup = {' ' : ' '}
        dict = 'abcdefghijklmnopqrstuvwxyz'
        l = 0
        for i in key:
            if i not in lookup:
                lookup[i] = dict[l]
                l += 1
        res = ''
        for i in range(len(message)):
            res += lookup[message[i]]
        return res
            