class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #we need to find the continuos string sequence 
        #first edge case , if the given string is less than 10 , return empty list 
        if len(s) < 10 :
            return []

        #initialize the sets to track seen and repeated 
        seen , repeated = set() , set()

        #iterate and scan with a window of 10 elements 
        for i in range(len(s) -9):
            sequence = s[i:i + 10]

            if sequence in seen :
                repeated.add(sequence)

            else:
                seen.add(sequence)

        return list(repeated)