class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hashSet = []
        for i in s:
            hashSet.append(i)
        for j in t:
            if j in hashSet:
                hashSet.remove(j)
            
        if (hashSet):
            return False
        else:
            return True
