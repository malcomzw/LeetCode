class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #use counters to count characters 
        textCount = Counter(text)
        balloon = Counter('balloon') #count the number of characters 

        result = len(text)
        # compare the ratios
        for c in balloon :
            result = min(result, textCount[c] // balloon[c])
        return result