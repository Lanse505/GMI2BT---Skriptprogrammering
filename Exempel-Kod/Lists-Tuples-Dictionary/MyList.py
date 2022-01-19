list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)

list2 = ['Red', 'Green', 'Blue']
for i in range(0, len(list2), 1):
    set = []
    entry = list2[i]
    set.append(entry.lower())
    set.append(list2[i])
    set.append(entry.upper())
    print(set)

input()