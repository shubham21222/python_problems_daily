def remove_duplicates(arr, n):
    if n == 0 or n == 1:
        return arr[:n]

    arr.sort()
    non_duplicates = [arr[0]]

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            non_duplicates.append(arr[i])

    return non_duplicates

arr1 = [1, 2, 3, 4, 2, 1]
n = 6
s1 = remove_duplicates(arr1, n)
print(s1)
