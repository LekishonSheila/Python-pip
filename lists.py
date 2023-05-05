# Write a Python program to get a single string from two given strings,
#  separated by a space, and swap the first two characters of each string
def swaped_strings(str1, str2):
    str1_first_two = str1[:2]
    str2_first_two = str2[:2]
    str1_swapped = str2_first_two + str1[2:]
    str2_swapped = str1_first_two + str2[2:]
    result = str1_swapped + ' ' + str2_swapped

    return result





# Write a Python function that takes a list of words and returns
#  the longest word and the length of the longest one
def longest_word(words):
    longest = ""
    length = 0

    for word in words:
        if len(word) > length:
            longest = word
            length = len(word)

    return longest, length

# Write a Python program that accepts a comma-separated sequence of words as input 
# and prints the distinct words in sorted form (alphanumerically).
words = input("Enter a comma-separated list of words: ")
words_list = words.split(",")
unique_words = sorted(set(words_list))
print("The distinct words in sorted form are: ")
print(", ".join(unique_words))

#  Write a Python function that takes two lists and returns 
# True if they have at least one common member.
def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
keys = ["Black", "Red", "Maroon", "Yellow"]
values = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = [{keys[i]: values[i]} for i in range(len(keys))]
print(result)


#  Write a Python program to check whether all dictionaries in a list are empty or not
def all_dicts_empty(lst):
    for d in lst:
        if bool(d):
            return False
    return True

# Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
def number(numbers):
 result = [num for num in number if num % 2 == 0]
 numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
 print(result)

#  Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common = []

for num_a in list_a:
    for num_b in list_b:
        if num_a == num_b:
            common.append(num_a)

print(common)

# Use a nested list comprehension to find all of the numbers from 1-1000 that
#  are divisible by any single digit besides 1 (2-9)
divisible = [num for num in range(1, 1001) if any(num % i == 0 for i in range(2, 10))]

print(divisible)


# Write a Python function to remove all vowels in a string
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)




   
