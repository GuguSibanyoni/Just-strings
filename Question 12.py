# algorithm to check string rotation


_string1 = "waterbottle"
_string2 = "erbottlewat"


def is_string_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = string1.lower()
    string2 = string2.lower()
    ch_indexes = [index for index, letter in enumerate(
        string2) if letter == string1[0]]
    if not ch_indexes:
        return False

    len_string1 = len(string1)

    for ch_ind in ch_indexes:
        for i in range(len_string1):
            if string2[(ch_ind + i) % len_string1] != string1[i]:
                break
            elif i == (len_string1 - 1):
                return True

    return False


print(is_string_rotation(_string1, _string2))
