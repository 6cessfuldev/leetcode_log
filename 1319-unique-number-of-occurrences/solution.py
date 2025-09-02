class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Best Solution
        counts = Counter(arr)
        set1 = set(counts.values())
        return len(set1) == len(counts)

        ## Solution1
        # my_map = {}

        # for num in arr:
        #     my_map[num] = my_map.get(num, 0) + 1

        # values = list(my_map.values())
        # return len(values) is len(set(values))

        
