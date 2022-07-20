"""1)Write a Python program to calculate the length of a string"""
str = "python"
print(len(str))

"""2) Write a Python program to count the number of characters (character frequency) in a string"""
s = input("enter any string : ")
ch = input("enter search character : ")
f = 0
for i in s:
    if i == ch:
        f = f + 1
print("number of time found = ", f) 

"""3).Write a Python program to get a string made of the first 2 and the last 2 chars 
from a given a string. If the string length is less than 2, return instead of the 
empty string."""
def string_both_ends(str):
    if len(str)<2:
        return ''
    return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

"""4)Write a Python program to get a string from a given string where all occurrences of its first 
char have been changed to '$', except the first char itself"""
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    return str1
print(change_char('restart'))

"""5)  Write a Python program to get a single string from two given strings, separated by a space 
and swap the first two characters of each string."""
def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

"""6)Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
 If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged."""
def add_string(str1):
    length = len(str1)
    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

"""7)Write a Python program to find the first appearance of the substring 'not' and 
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' 
substring with 'good'. Return the resulting string"""
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1
print(not_poor('the lyrics is not that poor!'))
print(not_poor('the lyrics is poor!'))

"""8) Write a Python function that takes a list of words and return the longest word 
and the length of the longest one."""
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["two", "seven", "exercise"])
print("\nlongest word: ", result[1])
print("length of the longest word: ", result[0])

"""9)Write a Python program to remove the nth index character from a nonempty 
string."""
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part + last_part
print(remove_char('python', 0))
print(remove_char('python', 3))
print(remove_char('python', 5))

"""10)Write a Python program to change a given string to a new string where the 
first and last chars have been exchanged."""
def change_string(str1):
    return str1[-1:] + str1[1:-1] + str1[:1]
print(change_string('6789'))
print(change_string('jklmn'))

"""11)Write a Python program to remove the characters which have odd index 
values of a given string"""
def odd_values_string(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
        return result
print(odd_values_string('python'))
print(odd_values_string('abwxyz'))

"""12)Write a Python program to count the occurrences of each word in a given 
sentence"""
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1 
        else:
            counts[word] = 1
    return counts
print(word_count('the quick brown fox over the lazy dog'))    

"""13)Write a Python script that takes input from the user and displays that input 
back in upper and lower cases"""
user_input = input("what is your favourite colour? ")
print("my favourite colour is", user_input.upper())
print("my favourite colour is", user_input.lower())

"""14). Write a Python program that accepts a comma separated sequence of words 
as input and prints the unique words in sorted form (alphanumerically)."""
items = input("input comma separated sequence of words ")
words = [word for word in items.spilt(",")]
print(",".join(sorted(list(set(words)))))

"""15)Write a Python function to create the HTML string with tags around the 
word(s)"""
def add_tags(tag, word):
    return "<%s>%s<%s>" % (tag, word, tag)
print(add_tags('i', 'python'))
print(add_tags('b', 'python class'))

"""16). Write a Python function to insert a string in the middle of a 
string."""
def insert_string_middle(str, word):
    return str[:2] + word + str[2:]
print(insert_string_middle('[[]]', 'python'))
print(insert_string_middle('{{}}', 'php'))

"""17)Write a Python function to get a string made of 4 copies of the last two 
characters of a specified string (length must be at least 2)"""
def insert_end(str):
    sub_str = str[-2:]
    return sub_str * 4
print(insert_end('python'))
print(insert_end('exercises'))

"""18)Write a Python function to get a string made of its first three characters of a 
specified string. If the length of the string is less than 3 then return the original 
string"""
def first_three(str):
    return str[:3] if len(str) > 3 else str
print(first_three('ipy'))
print(first_three('python'))

"""19)Write a Python program to get the last part of a string before a specified 
character."""
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])


"""20) Write a Python function to reverses a string if it's length is a multiple of 
4."""
name = input("enter a name: ")
if (len(name)%4==0):
    print(name[::-1])
else:
    print("can't")

"""21) Write a Python function to convert a given string to all uppercase if it contains 
at least 2 uppercase characters in the first 4 characters."""
str1 = input("please enter : ")
str2 = str1.upper()
print("\n oringinal = ", str1)
print("result = ", str2)

"""22)Write a Python program to remove a newline in Python"""
list = '\n python class room \n'
string = list.strip()
print(string)

"""23)write a Python program to check whether a string starts with specified 
characters"""
string = "python class"
print(string.startswith("pyt"))