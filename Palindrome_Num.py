#Determine whether an integer is a palindrome. Do this without extra space
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            
            return False
        a,b=x,0
        while a:
            b= b*10+ a%10
            a/=10
        return b==x
        """
        :type x: int
        :rtype: bool
        """
        
