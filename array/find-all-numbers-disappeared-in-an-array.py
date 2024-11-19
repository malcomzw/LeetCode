class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #MARK THE VISITED INDICES 
        for num in nums :
            #use the absolute value 
            index = abs(num)-1 
            nums[index ] = -abs(nums[index]) #mark as negative 

            #collect the missing numbers 
        result = []
            #iterate the whole range n 
        for i in range(len(nums)):
                if nums[i]> 0:
                    result.append(i + 1)
        return result