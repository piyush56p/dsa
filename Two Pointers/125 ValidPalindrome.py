class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = s.strip()
        s = re.sub('[^A-Za-z0-9]+', '', s)
        

       

        low = 0
        high = len(s) - 1
        while(low<=high):
            if(s[low] != s[high]):
                return False
            else:
                low = low+1
                high = high -1
            
        return True
        
        
        
