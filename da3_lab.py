#1
"""
Create a list of integers and find the sum of all even numbers.
Add a new element to the end of the list.
Remove the first element from the list.
Sort the list in ascending order.
"""
"""
# Create a list of integers
int_list = list(range(1, 100))
lSum = sum(int_list)
int_list.append(101)
int_list.remove(int_list[0])
sorted(int_list)
print(int_list)
"""

#2.
"""
Create a tuple containing names of your three favorite fruits.
Use tuple unpacking to assign each fruit to a separate variable.
Create a new tuple by concatenating your favorite fruits with a tuple of your favorite vegetables.
"""
"""
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "spinach", "cabbage")
f1, f2, f3 = fruits
fv = fruits + vegetables
print(fv)
"""

#3
"""
Create a list of strings and find the longest string.
Calculate the sum of a range of numbers from 1 to 100.
Using a list comprehension, create a list containing the squares of the numbers from 1 to 10.
"""
"""
strings = ["apple", "banana", "A", "Hello", "Python is fun!", "pineapple", "blueberry"]
lString = ""
for i in strings:
        if len(i) > len(lString):
            lString = i;
print(lString)
"""

#4
"""
Create two lists, a and b, where b is a shallow copy of a.
Modify an element in a and observe the effect on b.
Repeat the process using a deep copy instead of a shallow copy
"""
"""
import copy
a = [1, 2, [3, 4]]
b = a.copy()
str = 'a'
a.append(str)
#print(a)
#print(b)
b2 = a
b1 = copy.deepcopy(a)
print(a)
print(b)
print(b1)
print(b2)
"""
#5
"""
Create a string containing a sentence.
Reverse the order of the words in the sentence.
Convert the sentence to uppercase. Replace a word in the sentence with another word.
"""
"""
sentence = "This is a sample sentence"
list1 = sentence.split()
print(list1[::-1])
"""

#6
"""
A palindrome is a word, phrase, number, or other sequences of characters 
that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. 
Write a function that checks if a given string is a palindrome.
"""
"""
def is_palindrome(s: str):
    # Implement your code
    # Return true if s is palladium, false otherwise.
    p = True
    for x in input_strings:
        if x == s:
            p = True
            break
        else:
            p = False
    return print(p)

input_strings = ['racecar', 'hello', 'madam', 'python', 'level', 'world']
r_list = []

for i in input_strings:
    r_list = i[::-1]
    r_String = r_list
    is_palindrome(r_String)
"""

#Lab6
#1
"""
Create a list of numbers from 1 to 50.
Filter out all the numbers that are divisible by 3 and store them in a new list.
Calculate the sum of the remaining numbers in the original list.
Reverse the order of the elements in the original list.
"""
"""
numbers = list(range(1, 51))
newList = []
print("reversed order :",numbers[::-1])
for i in numbers:
    if i % 3 == 0:
        newList.append(i)
        numbers.remove(i)
print("3의 약수가 아닌 나머지 수들의 합 :",sum(numbers))
"""

#2
"""
Create a tuple containing 5 numbers.
Calculate the minimum, maximum, and average of the numbers in the tuple.
Create a new tuple by appending the calculated minimum, maximum, and average to the original tuple.
Use tuple unpacking to store the first three elements of the new tuple in separate variables.
"""
"""
numbers = (3, 7, 2, 9, 5)
print(max(numbers))
print(min(numbers))
print(sum(numbers) / len(numbers))

a,b,c = numbers[:3]
newNum = (a,b,c)
print(newNum)
"""

#4
"""
Write a function that takes a string as input and returns the string with all vowels removed.
Create a list of strings and use the function to filter the vowels from each string.
Sort the filtered strings based on the number of consonants.
Write a function that takes a string as input and returns the string with words in reverse order. Use this function on each string in the list of filtered strings.
"""
def remove_vowels(s):



# Create a list of strings
strings = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "strawberry", "avocado", "zucchini", "grape", "blueberry"]
