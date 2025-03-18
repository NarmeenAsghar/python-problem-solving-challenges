#--------------------Assignment 3: Problem-Solving Challenges (Class-4)

# 1- Reverse a String
'''Write a function that takes a string as input and returns the reversed string'''


#-----------SLICING:
'''
slicing is python's powerfull tool which can access sequence type(list, tuple, string) with specific range
(SYNTAX)-> sequence[start:end:step]     (GENERAL SYNTAX)-> variable_name[start:end:step]
The expression `[::-1]` reverses the string by using the default start and end, with a step of `-1`, which means it traverses the string in reverse order.
'''
value = "Pakistan"
reversed_value = value[::-1]
print(value)      # output----Pakistan
print(reversed_value)        # output----natsikaP


slang = "Long Live Pakistan"
reversed_slang = slang[::-1]
print(slang)        # output----Long Live Pakistan
print(reversed_slang)          # potput----natsikaP eviL gnoL


def fruit(f):
    return f[::-1]

print(fruit("apple"))        # Output----elppa



# 2- Count Vowels in a String
'''Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).'''

item = "Plate"
# contains uppercase and lowercase too
vowels = "AEIOUaeiou"
count = 0
for letter in item:
    if letter in vowels:
        count += 1
print(count)      # Output----2 (there are 2 vowels in item Plate)



# 3- Sum of Digits
'''Write a function that takes a non-negative integer and returns the sum of its digits.'''


digits = 458743
sum_of_digits = 0

# convert into string to acess digits easily
for digit in str(digits):
# converts into integer for addition
    sum_of_digits += int(digit)
print(sum_of_digits)       # output----31



def add_numbers(num):
    total = 0
    
# if num will contain value, loops continue
    while num > 0:
# modulus to remove last digit
        total += num % 10 
# division to remove last digit from num
        num = num // 10
# totaling
    return total
result = add_numbers(7846815)
print(result)       # Output----39

