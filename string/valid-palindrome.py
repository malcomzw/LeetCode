class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialize 2 pointers left and right 
        l,r = 0 , len(s)-1 

        #loop while 
        while l < r :
            #move the left pointer to the right without skipping aplphanumeric characters
            while l < r and not s[l].isalnum():
                l +=1
            while r > l and not s[r].isalnum():
                r-=1
            
            #check if the characters at both pointers are equal in lower case 

            if s[l].lower() != s[r].lower() :
                return False 
            
            #move the pointers for next comparison 

            l +=1
            r-=1 

        return True
