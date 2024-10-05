class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # use map as we have to keep count
        freq1 = [0]*26
        windowFreq = [0]*26
        for char in s1:
            freq1[ord(char)-97]+=1
        for i in range(0, len(s1)):
            print(i)   
            windowFreq[ord(s2[i])-97]+=1
        
        for i in range(len(s1), len(s2)):
            print(i)
            if freq1 == windowFreq:
                return True

            # Slide window and reduce windowFreq
            windowFreq[ord(s2[i - len(s1)])-97]-=1
            windowFreq[ord(s2[i])-97]+=1
        return False

s1,s2 = "adc",  "dcda"
sol = Solution()
print(sol.checkInclusion(s1,s2))