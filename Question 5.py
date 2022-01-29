# Given an array of integers, every element appears twice except for one. Find that single one

numbers = [1, 2, 2, 3, 1]
answer = 0

for i in range(len(numbers)):
    answer ^= numbers[i]

print(answer)