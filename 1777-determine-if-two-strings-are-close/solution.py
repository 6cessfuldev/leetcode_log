class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(word1)):
            map1[word1[i]] = map1.get(word1[i], 0) + 1
            map2[word2[i]] = map2.get(word2[i], 0) + 1

        return sorted(map1.keys()) == sorted(map2.keys()) and sorted(map1.values()) == sorted(map2.values())
