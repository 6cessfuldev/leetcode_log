class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        t_length = len(t)
        s_length = len(s)
        pointer_left = 0
        pointer_right = t_length-1
        left_idx = 0
        right_idx = s_length-1

        while (pointer_left <= pointer_right) and (left_idx <= right_idx):
            # 오른쪽에서 체크
            if t_length//2 - pointer_left <= pointer_right - t_length//2:
                if s[right_idx] == t[pointer_right]:
                    pointer_right -= 1
                    right_idx -= 1
                else:
                    pointer_right -= 1

            # 왼쪽에서 체크
            else:
                if s[left_idx] == t[pointer_left]:
                    pointer_left += 1
                    left_idx += 1
                else:
                    pointer_left += 1
        print(left_idx)
        print(right_idx)
        return left_idx > right_idx
