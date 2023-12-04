class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_int  = ''

        for i in range(len(num)-2):
            current_str = num[i:i+3]

            if current_str[0]==current_str[1]==current_str[2]:
                max_good_int = max(max_good_int,current_str)

        return  max_good_int