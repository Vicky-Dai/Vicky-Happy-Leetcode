from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote:str, magazine:str) -> bool:

        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            value = hashmap.get(x) #Return the value for key if key is in the dictionary, else default. 
            if not value:
                return False #终止
            else:
                hashmap[x] -= 1

        return True



