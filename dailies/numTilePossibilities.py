class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        used = [False] * n
        seen = set()
        
        def backtrack(curr):
            # What is the base case?
            if curr:
                seen.add("".join(curr))
            for idx, val in enumerate(tiles):
                if used[idx]:
                    continue
                # Do something
                used[idx] = True
                # Backtrack
                backtrack(curr + val)
                # Undo something
                used[idx] = False
        backtrack('')
        return len(seen)
            

sol = Solution()
print(sol.numTilePossibilities("V"))
print(sol.numTilePossibilities("AB"))
print(sol.numTilePossibilities("AAB"))
print(sol.numTilePossibilities("AAABBC"))