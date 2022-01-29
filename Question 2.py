# Algorithm To determine if two strings are anagrams of each other

def check(string1, string2):
 
    
    if set(string1.replace(" ", "").lower()) == set(string2.replace(" ", "").lower()):
      print("The strings are anagrams.")
    else:
      print("The strings aren't anagrams.")
    


if __name__ == '__main__':
    word1, word2 = 'Khanyisile', 'Khanyi Isle'
    check(word1, word2)