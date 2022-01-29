# To determine if two given strings, is one a permutation of the other


string1 = "Khanyisile"
string2 = "khanyi sile"

def is_Permutation(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    if len(string1) != len(string2):
        return False

    for i in string1:
        if i in string2:
            string2 = string2.replace(i, "")
    return len(string2) == 0

print(is_Permutation(string1, string2))


'''
Ask the interviewwer if empty spaces are considered as characters or not
Ask if we are to keep the case the same or are allowed to change it (case sensitivity)

'''