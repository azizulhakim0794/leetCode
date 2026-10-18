# Beginner
# 1. Print "Hello, World!".
# print("Hello, World!")

# 2. Take two numbers as input and print their sum.
# firstNum = int(input("Enter first Numner:"))
# secondNum = int(input("Enter second Numner:"))


# class AddNums:
#     def __init__(self, firstN, secondN):
#         self.firstN = firstN
#         self.secondN = secondN

#     def add_two_number(self):
#         return self.firstN + self.secondN


# add_nums = AddNums(firstNum, secondNum)

# result = add_nums.add_two_number()

# print(result)

# 3. Check whether a number is even or odd.
# num = int(input("Enter Numner:"))


# class FindEvenOrOddNums:
#     def __init__(self, nums):
#         self.nums = nums

#     def find_even_or_odd(self):
#         if self.nums == 0 or self.nums < 0:
#             print("Enter a valid positive number")
#             return
#         if self.nums % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")


# add_nums = FindEvenOrOddNums(num)
# add_nums.find_even_or_odd()

# 4. Find the largest of three numbers.

# num1 = int(input("Enter first numner:"))
# num2 = int(input("Enter second numner:"))
# num3 = int(input("Enter third numner:"))


# class FindLargestNumber:
#     def __init__(self, num1, num2, num3):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3

#     def find_lagest_number(self):
#         if self.num1 > self.num2 and self.num1 > self.num3:
#             print(f"The largest number is {self.num1}")
#         if self.num2 > self.num3 and self.num3 > self.num1:
#             print(f"The largest number is {self.num2}")
#         if self.num3 > self.num2 and self.num2 > self.num1:
#             print(f"The largest number is {self.num3}")

#         else:
#             print(f"some of you number are equel {self.num1}, {self.num2}, {self.num3}")


# add_nums = FindLargestNumber(num1, num2, num3)
# add_nums.find_lagest_number()

# 5. Calculate the factorial of a number.


# num = int(input("Enter Numner:"))


# class Factorial:
#     def __init__(self, nums):
#         self.nums = nums

#     def calculate(self):
#         if self.nums < 0:
#             print("enter a valid positive number")
#             return

#         x = 1
#         for i in range(1, self.nums + 1):
#             x = x * i
#         print(x)


# result = Factorial(num)
# result.calculate()


# 6. Print numbers from 1 to 10 using a for loop.


# class Looping:

#     def loop_nums(self):
#         for i in range(1, 11):
#             print(i)


# result = Looping()
# result.loop_nums()

# 7. Print the multiplication table of a given number.

# num = int(input("Enter Numner:"))


# class Multiplication:
#     def __init__(self, nums):
#         self.nums = nums

#     def calculate(self):
#         if self.nums == 0 or self.nums < 0:
#             print("enter a valid positive number")
#             return

#         for i in range(1, 11):
#             print(f"{self.nums} x {i} = {self.nums * i}")


# result = Multiplication(num)
# result.calculate()

# 8. Calculate the sum of all numbers in a list.

# num = [2, 3, 5, 6]


# class SumOfList:

#     def __init__(self, nums):
#         self.nums = nums

#     def calculate(self):
#         sum = 0
#         for i in range(len(self.nums)):
#             sum = sum + self.nums[i]
#         print(sum)


# result = SumOfList(num)
# result.calculate()

# 9. Reverse a string without using [::-1].

# num = [2, 3, 5, 6, 4, 7, 8, 9]


# class ReverseList:

#     def __init__(self, nums):
#         self.nums = nums

#     def rotate(self):
#         ans = []
#         for i in range(len(self.nums)):
#             item = len(self.nums) - i

#             ans.append(self.nums[item - 1])
#         print(ans)


# result = ReverseList(num)
# result.rotate()

# 10. Count the number of vowels in a string.
# text = "HeLLo world"


# class FindVowels:

#     def __init__(self, texts):
#         self.texts = texts

#     def calculate_vowels(self):
#         count = 0
#         for i in range(len(self.texts)):
#             text = self.texts[i].casefold()
#             if text == "a" or text == "e" or text == "i" or text == "o" or text == "u":
#                 count += 1
#         print(count)


# result = FindVowels(text)
# result.calculate_vowels()


# Intermediate
# 11. Find the largest number in a list without using max().

# num = [-9, 0, -1, 2, 3, 5, 6, 4, 7, 8, 9]


# class MaxNumbers:

#     def __init__(self, nums):
#         self.nums = nums

#     def calculate(self):
#         ans = self.nums[0]
#         for i in range(len(self.nums)):
#             if self.nums[i] > ans:
#                 ans = self.nums[i]

#         print(ans)


# result = MaxNumbers(num)
# result.calculate()

# 12. Remove duplicate elements from a list.

# num = [-9, 0, -1, 2, 3, 5, 2, 5, 6, 4, 7, 8, 9]


# class RemoveDuplicate:

#     def __init__(self, nums):
#         self.nums = nums

#     def calculate(self):
#         ansList = []
#         for num in self.nums:
#             if num not in ansList:
#                 ansList.append(num)
#         print(ansList)


# result = RemoveDuplicate(num)
# result.calculate()

# 13. Check whether a string is a palindrome.

# text = "Madam"


# class CheckPalindrome:

#     def __init__(self, texts):
#         self.texts = texts

#     def calculate_word(self):

#         main_text = self.texts
#         texts = [char.lower() for char in main_text if char.isalnum()]
#         cleaned_texts = "".join(texts)
#         left = 0
#         right = len(cleaned_texts) - 1
#         print(texts)
#         for i in range(len(cleaned_texts)):
#             left_text = cleaned_texts[left]
#             right_text = cleaned_texts[right]
#             if left_text != right_text:
#                 print(False)
#                 return
#             left += 1
#             right -= 1

#         print(True)


# result = CheckPalindrome(text)
# result.calculate_word()

# 14. Convert a list of digits into a single integer.

# num = [2, 3, 5, 6]


# class ConvertList:

#     def __init__(self, nums):
#         self.nums = nums

#     def calculateList(self):
#         sum = ""
#         for i in self.nums:
#             sum += str(i)
#         print(int(sum))


# result = ConvertList(num)
# result.calculateList()
# Example: [1, 2, 3, 4] → 1234

# 15. Create a Student class with __init__() and a method that prints the student's name and age.


# class Student:

#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def stduents_details(self):
#         print(f"The student's name is {self.name} and student's age is {self.age}")


# result = Student("Jashim", 17)
# result.stduents_details()

# main_text = "A man, a plan, a canal: Panama"


# print(cleaned_texts)
