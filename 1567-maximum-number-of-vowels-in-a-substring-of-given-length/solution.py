class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ptr = 0
        window = s[0:k]
        max_v_cnt = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        while ptr <= len(s) - k:
            # print(window)
            max_v_cnt = max(max_v_cnt, sum(window.count(v) for v in vowels))

            ptr += 1
            if ptr <= len(s) - k:
                window = window[1:] + s[ptr+k-1]

                
        return max_v_cnt
