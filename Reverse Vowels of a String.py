class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")
        strArr = list(s)
        left = 0
        right = len(strArr)- 1

        while left < right:
            if strArr[left] not in vowels:
                left += 1
                continue
            if strArr[right] not in vowels:
                right -= 1
                continue

            strArr[left], strArr[right] = strArr[right],strArr[left]
            left += 1
            right -= 1

        return "".join(strArr)

            
