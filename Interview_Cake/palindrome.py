class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        end = len(A) - 1
        start = 0
        if not A:
            return 1
        while start < end:
            if A[start].isalnum() and A[end].isalnum():
                ast = A[start].lower()
                aen = A[end].lower()
                if ast != aen:
                    return 0
                else:
                    start += 1
                    end -= 1
            elif not A[start].isalnum():
                start += 1
            elif not A[end].isalnum():
                end -= 1

        return 1

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        s = A.lower()
        s = s.replace(',','')
        s = s.replace(' ','')
        s = s.replace(':','')
        s = s.replace(';','')
        s = s.replace('?','')
        s = s.replace('!','')
        s = s.replace('&','')
        s = s.replace('(','')
        s = s.replace(')','')
        s = s.replace(']','')
        s = s.replace('[','')
        s = s.replace("'",'')
        s = s.replace('"','')
        if s[::-1] == s:
            return 1
        else:
            return 0


class Solution:

    def isAlphaNumeric(self, c):
        return (c >= 'a' and c <= 'z') or (c >= '1' and c <= '9')

    # @param A : string
    # @return an integer
    def isPalindrome(self, A):

        i = 0
        j = len(A) - 1

        A = A.lower()

        while i < j:
            while i < len(A) - 1 and not self.isAlphaNumeric(A[i]):
                i = i + 1

            while j > 0 and not self.isAlphaNumeric(A[j]):
                j = j - 1

            if self.isAlphaNumeric(A[i]) and self.isAlphaNumeric(A[j]) and A[i] != A[j]:
                return 0

            i += 1
            j -= 1

        return 1