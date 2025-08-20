class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        str_arr = list(str(x))

        for i in range(len(str_arr)//2):
            if str_arr[i] == str_arr[len(str_arr) - 1 - i]:
                continue
            else:
                return False

        return True
