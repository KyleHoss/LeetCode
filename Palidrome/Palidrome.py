class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            input = list(map(int,str(x)))
        except:
            # print('False')
            return False
        if input == input[::-1]:
            # print('True')
            return True
        else: 
            # print('False')
            return False
        