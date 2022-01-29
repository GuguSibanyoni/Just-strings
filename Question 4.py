# Algorithm to determine if a string is palindrome.


import string


def is_Palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    
    punctuation_List = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
    for i in punctuation_List:
        for i in string:
            string = string.replace(i,'')
    

    return string == string[::-1]


string1 = "Sis"
string2 = "CIVIC"
string3 = "Madam, in Eden, I'm Adam."

print(is_Palindrome(string1))
print(is_Palindrome(string2))
print(is_Palindrome(string3))