class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                if asteroid > 0 or stack[-1] * asteroid > 0:
                    stack.append(asteroid)
                else:
                    while stack and stack[-1] <= -asteroid:
                        if stack[-1] * asteroid > 0:
                            stack.append(asteroid)
                            break
                        if stack[-1] == -asteroid:
                            stack.pop()
                            break
                        else:
                            stack.pop()

                        if not stack:
                            stack.append(asteroid)
                            break

        return stack
