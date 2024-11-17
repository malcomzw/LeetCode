class Solution:
    def firstUniqChar(self, s: str) -> int:
        #build hashmap with default dict 
        count = defaultdict(int)

        for c in s :
            count[c] +=1 

        #step 2 , find the first unique char 
        for i,c in enumerate(s):
            if count[c] ==1 :
                return i
        return -1 
        