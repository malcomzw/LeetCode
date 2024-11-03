class Solution:
    def isHappy(self, n: int) -> bool:
        #use a helper function to calculate the sum of squares 

        def sumOfsquares (number:int) -> int:
            total_sum = 0 #total sum 
            while number> 0:
                #extract the last value 
                digit = number % 10 
                total_sum += digit **2
                number //= 10
            return total_sum 

        # initialize 2 pointers to iterate the numbers given 
        fast = n 
        slow = n 

        #move the pointers 
        while True : 
            slow = sumOfsquares(slow)
            fast = sumOfsquares(sumOfsquares(fast))

            if fast ==1 :
                return True 

            if fast  == slow :
                return False #cycle has been detected 