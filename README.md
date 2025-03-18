# Assignment 3: Problem-Solving Challenges (Class-4) ⚡💻

This repository contains solutions to three common programming challenges related to strings and numbers. Each problem is solved using Python functions. Below are the challenges and their respective solutions:

---

## 1. Reverse a String 🔄

### Problem Statement:
Write a function that takes a string as input and returns the reversed string. 

### Solution:
This problem is solved using Python's powerful slicing technique. The expression `[::-1]` is used to reverse the string.

### Explanation:
- `[::-1]` slices the string from the end to the beginning, effectively reversing the string. 🔄

---

## 2. Count Vowels in a String 🅰️

### Problem Statement:
Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive). 

### Solution:
We loop through each letter in the string and check if it belongs to the set of vowels (both lowercase and uppercase).

### Explanation:
- The function checks if each character in the string is a vowel by checking membership in the string `vowels`. 🅰️

---

## 3. Sum of Digits ➕

### Problem Statement:
Write a function that takes a non-negative integer and returns the sum of its digits.

### Solution:
We can solve this by converting the number to a string and iterating over each character to sum the digits.

### Explanation:
- The function uses the modulus operator (`%`) to extract the last digit of the number and adds it to the total. ➕
- Then, the number is reduced by performing integer division (`//`) to remove the last digit.

---

## How to Run the Code: 💻

1. Copy the code from the Python functions provided in the repository.
2. Run the code in any Python 3.x environment.

---

## Conclusion: 🎉

This assignment demonstrates basic Python concepts such as string manipulation, loops, and functions. The solutions provided are simple yet effective approaches to solving the problems. 
