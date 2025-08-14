class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # membership O(1)
        chars = list(s)             # 문자열 -> 리스트로

        ptr1, ptr2 = 0, len(chars) - 1
        while ptr1 < ptr2:
            if chars[ptr1] not in vowels:
                ptr1 += 1
                continue
            if chars[ptr2] not in vowels:
                ptr2 -= 1
                continue

            chars[ptr1], chars[ptr2] = chars[ptr2], chars[ptr1]
            ptr1 += 1
            ptr2 -= 1

        return ''.join(chars)

