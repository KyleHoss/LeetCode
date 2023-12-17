
def romanToInt(s: str) -> int:
    
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum=0
    num = [0] * (len(s)+1)
    for i in range(len(s)-1,-1,-1):
        num[i] = roman[s[i]]
        if  num[i+1] > num[i]:
            sum = sum - num[i]
        else:
            sum = sum + num[i]
    print(sum)

romanToInt("LVIII")



class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        num = [0] * (len(s)+1)
        for i in range(len(s)-1,-1,-1):
            num[i] = roman[s[i]]
            if  num[i+1] > num[i]:
                sum = sum - num[i]
            else:
                sum = sum + num[i]
        return sum