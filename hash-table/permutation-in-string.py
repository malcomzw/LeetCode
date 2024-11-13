class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge cas 1 if thepermutation ddoesnt exist 
        if len(s1) > len(s2) :
            return False

        #frequency counters 
        s1_count = [0] * 26
        s2_count = [0] * 26 

        #fill in s1 and the first part of s2  
        for i in range(len(s1)):
            s1_count[ord(s1[i])- ord('a')] +=1
            s2_count[ord(s2[i])- ord('a')] +=1 

        #slide the window across s2 
        for i in range(len(s1), len(s2)):
            if s1_count == s2_count :
                return True
            #update s2 counter 
            s2_count[ord(s2[i])- ord('a')] +=1
            #remove the outgoing letter 
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -=1

            #check the last window 
        return s1_count == s2_count

            
