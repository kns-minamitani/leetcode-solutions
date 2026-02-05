class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        first = set('qwertyuiopQWERTYUIOP')
        second = set('asdfghjklASDFGHJKL')
        third = set('zxcvbnmZXCVBNM')
        for st in words:
            i = 0
            if st[i] in first:
                ref = first
            elif st[i] in second:
                ref = second
            else:
                ref = third
            
            while i < len(st) and st[i] in ref:
                i += 1
            
            if i == len(st):
                result.append(st)
        return result