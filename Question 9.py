# how to turn a string into a URL (we need to replace blank spaces with %20)

string1 = "Gugu's Lamb stew recipe"
string1_length = len(string1)

def make_URL(string, string_length):
    blankSpace = " "
    for i in range(string_length):
        if string1[i] == " ":
            blankSpace += "%20"
        else:
            blankSpace = blankSpace + string[i]
    return blankSpace

print(make_URL(string1, string1_length))
