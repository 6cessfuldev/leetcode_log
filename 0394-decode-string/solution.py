class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        digit_stack = []
        depth = 0
        num_str = ''

        str_stack.append('')

        for char in s:
            if char.isdigit():
                    num_str += char

            elif char == '[':
                digit_stack.append(int(num_str))
                num_str = ''
                # 부분 문자열 시작 
                str_stack.append('')

            elif char == ']':
                # 부분 문자열 끝
                tmp_str = str_stack.pop()
                tmp_dig = digit_stack.pop()
                str_stack[-1] += tmp_str * tmp_dig 
            else:
                # 문자열 더하기
                str_stack[-1] += char

        return str_stack[0]

