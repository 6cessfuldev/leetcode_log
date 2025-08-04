class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ### Thrid Answer

        for ch in set(ransomNote):
            if ransomNote.count(ch)>magazine.count(ch):
                return False
        return True


        ### Sencond Answer

        # for char in ransomNote:
        #     if char in magazine:
        #         magazine = magazine.replace(char, "", 1)
        #     else:
        #         return False
        # return True


        ### First Answer

        # map: Dict[str, int] = {}

        # for char in magazine:
        #     map[char] = map.get(char, 0) + 1

        # for char in ransomNote:
        #     if map.get(char, 0) == 0:
        #         return False
        #     else:
        #         map[char] -= 1

        # return True
