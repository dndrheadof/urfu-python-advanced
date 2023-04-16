def find_insert_position(array, inserted):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == inserted:
            return mid
        elif array[mid] < inserted:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


A = [1, 2, 3, 3, 3, 5]
x = 4
print(find_insert_position(A, x))
