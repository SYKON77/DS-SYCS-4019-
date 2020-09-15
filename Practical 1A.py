def searching(n, list1):
    size_of_list = len(list1)
    print("searching {} in list {}".format(n, list1))
    if n not in list1:
        print(n, "is not in the list")
    else:
        for i in range(size_of_list):
            if list1[i] == n:
                print("index of ", n, " is ", i)


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def InsertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i-1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = temp

        return array


def merging(list11, list12):
    print("merging..{} and {}".format(list11, list12))
    lst2 = [6, 3, 45, 23, 56, 67, 77, 65]
    print("list1 = ", list11)
    print("list2 = ", list12)
    merge = list11+list12
    return merge


def revrse(list1):
    print("reversig {}".format(list1))
    size = len(list1)-1
    i = 0
    while size > 0:
        list1[i], list1[size] = list1[size], list1[i]
        size -= 1
        i += 1
        if size <= i:
            break
    return list1


def main():
    list11 = [23, 45, 32, 34, 55, 66, 2, 33, 12, 3, 4]
    list12 = [23, 42, 12, 34, 33, 22, 11, 44, 33, 45, 67]
    print("given main list {}".format(list11))
    element_to_search = int(input("enter the number to search: "))
    searching(element_to_search, list11)
    print("\n")
    print("original list {}".format(list11))
    sorted_list = bubbleSort(list11)
    print("sorted list {}".format(sorted_list))
    print("\n")
    merged_list = merging(list11, list12)
    print("mergelist {}".format(merged_list))
    print("\n")
    reversed_list = revrse(list12)
    print("reversed list {}".format(reversed_list))


main()
