import sys
read = sys.stdin.readline

class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict1 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        num_dict2 = {'x':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        str_list = list(s)
        sum = 0
        for i in range(len(str_list)-1):
            if str_list[i]+str_list[i+1] in num_dict1.keys():
                sum += num_dict1[str_list[i]+str_list[i+1]]
                str_list[i] = 'x'
                str_list[i+1] = 'x'
        for e in str_list:
            sum += num_dict2[e]
        return sum

input_str = read().rstrip()
mod = Solution()
print(mod.romanToInt(input_str))
