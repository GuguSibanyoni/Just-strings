"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters.

If the"compressed" string would not become smaller than
the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a-z).
"""

from markupsafe import string


string1 = "abbcccddddaaa"
string2 = "aaaaaabbccbcaabb"
string3 = "abcdefg"


def string_Compression(_string):
    compressed_String = ""
    count = 1
    for i in range(len(_string)-1):
        if  _string[i] == _string[i+1]:
            count += 1
        else:
            compressed_String += _string[i] + str(count)
            count = 1
    compressed_String += _string[i] + str(count)

    if len(compressed_String) >= len(_string):
        return  _string
    else:
        return compressed_String

print(string_Compression(string1))
print(string_Compression(string2))
print(string_Compression(string3))