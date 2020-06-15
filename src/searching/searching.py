def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # the middle is the average of high and low
        mid = (high + low) // 2
        # check if the middle is the target
        if arr[mid] == target:
            return mid
        # if middle is higher, assign lower half
        elif arr[mid] < target:
            # +1 because it's already confirmed greater than what was at middle
            low = mid + 1
        else:
            # if middle is lower, move forwards
            # -1 because already confirmed the mid is lower than the target
            high = mid - 1

    return -1
