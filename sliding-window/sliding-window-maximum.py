class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #edge case , when the list is empty or k = 0
        if not nums or k == 0:
            return []

        #variables
        #deque to store the indices 
        deq = deque()
        result = []

        #iterate through the array 
        for i in range(len(nums)):            
            #if the index at the current element is out of window
            if deq and deq[0] < i -k +1: #comparing the indices size
                deq.popleft()   #removing the left most value 

            #remove the elements that are less than the current values
            while deq and deq[-1] < nums[i]:
                deq.pop()

            #add the current element to the deque 
            deq.append(i)

            #append the max value of the window to result 
            if i > k - 1:
                result.append(nums[deq[0]])
        return result


            

        


