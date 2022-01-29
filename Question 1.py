# Algorithm to determine if a string has all unique characters


def is_Unique(string):
    return len(string) == len(set(string))


string1 = "Gugu"
string2 = "Caroline"

print(is_Unique(string1))
print(is_Unique(string2))


'''
what I did here is use the set function and i did that because sets dont repeat values/characters
and you notice i use len as length. If all the characters is a string a unique the the lengths of the 
string and set should  equal.
string one however will produce a string length of 4 and a set length of 3 because G and g are different
which brings me to the idea that also using the .lower() function is great just to be thorough

i.e
def is_Unique(string):
    return len(string) == len(set(string.lower()))
'''