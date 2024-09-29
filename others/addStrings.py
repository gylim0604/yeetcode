class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = '';
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:  # Loop until either string reaches the end
            val1 = int(num1[i]) if i >=0 else 0;
            val2 = int(num2[j]) if j >=0 else 0;
            sum = val1 + val2 +  carry
            carry = sum //10
            res = str(sum%10) + res
            i -= 1
            j -= 1
        
        return res
            

num1 = "9";
num2 = "1";
sol = Solution()
print(sol.addStrings(num1,num2))