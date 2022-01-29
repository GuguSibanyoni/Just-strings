# algorithm for checking anagram

def check_Anagram(string1, string2):
    
    if len(string1.replace(" ", "").lower()) == len(string2.replace(" ", "").lower()):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

if __name__ == '__main__':
    word1, word2 = 'Khanyisile', 'Khanyi Isle'
    check_Anagram(word1, word2)