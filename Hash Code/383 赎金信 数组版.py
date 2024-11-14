class Solution:
    def canConstruct(self, ransomNote: str, magazine:str) -> bool:
        ransom_count = [0] *26
        magazine_count = [0] * 26
        for i in ransomNote:
            ransom_count[ord(i) - ord('a')] += 1
        for i in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))
    #all 函数    if all elements of the iterable are true return true 
    
        