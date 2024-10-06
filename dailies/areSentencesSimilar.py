class Solution:
    def areSentencesSimilar(self, s1: str,s2: str) -> bool:
        if(s1 == s2):
            return True
        arr1, arr2 = s1.split(), s2.split()
        len1, len2 = len(arr1) , len(arr2) 
        # edge case for empty string
        if(len1 ==0 or len2 ==0):
            return arr1[0] == arr2[0] or arr1[len1] == arr2[len2]
        
        prefix = 0
        suffix1, suffix2 = len1 -1 , len2 -1
        # check for prefix
        while  prefix < len1 and prefix < len2 and arr1[prefix] == arr2[prefix] :
            prefix+=1
        while suffix1 >= prefix and suffix2 >= prefix and arr1[suffix1] == arr2[suffix2]:
            suffix1-=1
            suffix2-=1
        
        return suffix1 < prefix or suffix2 < prefix


sol = Solution() 
s1,s2 = "My name is Haley","My Haley"
print(sol.areSentencesSimilar(s1,s2))
s1,s2 = "of","A lot of words"
print(sol.areSentencesSimilar(s1,s2))
s1,s2 = "Eating right now","Eating"
print(sol.areSentencesSimilar(s1,s2))
s1,s2 ="c h p Ny","c BDQ r h p Ny"
print(sol.areSentencesSimilar(s1,s2))
s1,s2 ="a BaabbAABbBbbaAb","a BbbA baaaaBaAabB bbab AaAB"
print(sol.areSentencesSimilar(s1,s2))
s1,s2 ="aa aa","aa aa A"
print(sol.areSentencesSimilar(s1,s2))