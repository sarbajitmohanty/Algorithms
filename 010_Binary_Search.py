# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    poteltialMatch = array[middle]
    if target == poteltialMatch:
        return middle
    elif target < poteltialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


# O(log(n)) time | O(1) space
def binarySearch2(array, target):
    return binarySearchHelper2(array, target, 0, len(array) - 1)

def binarySearchHelper2(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        poteltialMatch = array[middle]
        if target == poteltialMatch:
            return middle
        elif target < poteltialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1