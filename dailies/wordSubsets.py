class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        max_freq = {}
        res = []
        # map out the max frequency we need to check
        for word in words2:
            curr_freq = {}
            for char in word:
                curr_freq[char] = curr_freq.get(char,0) + 1
            for key, value in curr_freq.items():
                max_freq[key] = max(max_freq.get(key, 0),value)
        
        for word in words1:
            curr_freq = {}
            for char in word:
                curr_freq[char] = curr_freq.get(char,0) + 1
            
            for key, value in max_freq.items():
                if curr_freq.get(key,0) < value:
                    break
            else:  # This else executes only if the loop didn't break
                res.append(word)
        return res

sol = Solution()
print(sol.wordSubsets(['abc', 'abbcc'],["abc", "bb", "cc"]))