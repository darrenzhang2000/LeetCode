class Solution:
    '''
    time: O(n^2)
    '''
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ""
        i = 0
        while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
            i += 1
        for j in reversed(range(i)):
            if self.gcds(str1, str1[0:j + 1]) and self.gcds(str2, str1[0:j + 1]):
                return str1[0:j + 1]
        return ""
    
    def gcds(self, string, substr):
        mul = len(string) // len(substr)
        return string == mul * substr
        
        
        
