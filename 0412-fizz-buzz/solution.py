class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        
        for i in range(1, n+1):
            el = ""
            if i%15 == 0:
                el = "FizzBuzz"
            elif i%5 == 0:
                el = "Buzz"
            elif i%3 == 0:
                el = "Fizz"
            else:
                el = str(i)

            output.append(el)

        return output



        
