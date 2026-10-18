class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_texts = "".join([char.lower() for char in s if char.isalnum()])
        left = 0
        right = len(cleaned_texts) - 1
        for i in range(len(cleaned_texts)):
            if cleaned_texts[left] != cleaned_texts[right]:
                return False

            left += 1
            right -= 1
        return True
