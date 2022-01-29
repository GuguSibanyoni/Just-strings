# Finding the median


'''
sorting functiong without using sort() or sorted()

new_List = [l1, l2, l3]

for i in range(len(A1)):
    for j in range(i + 1, len(A1)):

        if new_List[i] > [j]:
            new_List[i], new_List[j] = new_List[j], new_List[i]

print(Numbers)
'''


def median_matrix(A):
    if len(A) == 1:
        _vector = sorted(A[0])
        return _vector[len(_vector)//2]
    else:
        new_List = []
        for row in range(len(A)):
            new_List.extend(A[row])
        new_List = sorted(new_List)
    return new_List[len(new_List)//2]



l1 = [1, 3, 5]
l2 = [2, 6, 9]
l3 = [3, 6, 9]
A1 = [l1, l2, l3]


A2 = [l1]

print(median_matrix(A1))
print(median_matrix(A2))