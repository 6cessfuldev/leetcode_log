from collections import defaultdict

class Solution:
    def compress(self, chars: List[str]) -> int:
        my_map = defaultdict(int)
        
        i = 0
        while i < len(chars):
            if i == 0:
                my_map[chars[i]] = 1
                i += 1
                continue

            # 연속된 문자가 아닌 경우
            if i > 0 and chars[i] != chars[i-1]:
                if my_map[chars[i-1]] > 1:
                    arr = list(str(my_map[chars[i-1]]))
                    
                    my_map[chars[i-1]] = 0
                    my_map[chars[i]] = 1

                    chars[i: len(arr)] = arr
                    i += len(arr)+1
                else:
                    my_map[chars[i]] = 1
                    i += 1


            # 연속된 문자열이라면
            else:
                my_map[chars[i]] += 1
                del chars[i]
        
        if my_map[chars[i-1]] > 1:
            arr = list(str(my_map[chars[i-1]]))
            chars.extend(arr)

        return len(chars)
