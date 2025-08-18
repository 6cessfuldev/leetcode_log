class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min = 0
        i = 0
        j = 0

        if len(nums) < 3:
            return False

        if nums[0] < nums[1] & nums[1] < nums[2]:
            return True

        if nums[0] < nums[1]:
            j = 1

        for idx in range(1,len(nums),1):
            # 이미 i j 오름차순되어 있는 경우
            if j != 0:

                # nums[j] < nums[idx] 이면 합격
                if nums[j] < nums[idx]:
                    return True

                # nums[idx] 가 nums[i]와 nums[j] 사이라면 idx가 j로
                if nums[i] < nums[idx] & nums[idx] <= nums[j]:
                    j = idx
                
                # nums[i] >= nums[idx] 이면 최소값과 비교
                if nums[i] >= nums[idx]:
                    if nums[min] >= nums[idx]:
                        min = idx
                    else:
                        i = min
                        j = idx
            
            # 아직 j가 없을 경우
            else:
                if nums[i] < nums[idx]:
                    j = idx
                # nums[i] >= nums[idx] 인 경우 2차 i로 설정
                else:
                    i = idx
                    min = idx

        return False


