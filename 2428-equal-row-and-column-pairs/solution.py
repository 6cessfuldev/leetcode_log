class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = list(zip(*grid))

        return sum(1 for row in grid for col in cols if tuple(row) == col)

        # # 열 추출
        # columns = defaultdict(list)
        # for row in grid:
        #     for i in range(len(row)):
        #         columns[i].append(row[i])
        # cols = list(columns.values())
        
        # # row와 col 비교
        # return sum(1 for row in grid for col in cols if row == col)
