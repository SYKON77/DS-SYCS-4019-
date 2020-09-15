def searching(n, lst):
    size_of_list = len(lst)
    print("searching {} in list {}".format(n, lst))
    if n not in lst:
        print(n, "is not in the list")
    else:
        for i in range(size_of_list):
            if lst[i] == n:
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


def merging(lst1, lst2):
    print("merging..{} and {}".format(lst1, lst2))
    list2 = [6, 3, 45, 23, 56, 67, 77, 65]
    print("list1 = ", lst1)
    print("list2 = ", lst2)
    merge = lst1+lst2
    return merge


def revrse(lst):
    print("reversig {}".format(lst))
    size = len(lst)-1
    i = 0
    while size > 0:
        lst[i], lst[size] = lst[size], lst[i]
        size -= 1
        i += 1
        if size <= i:
            break
    return lst


def main():
    lst1 = [23, 45, 32, 34, 55, 66, 2, 33, 12, 3, 4]
    lst2 = [23, 42, 12, 34, 33, 22, 11, 44, 33, 45, 67]
    print("given main list {}".format(lst1))
    element_to_search = int(input("enter the number to search: "))
    searching(element_to_search, lst1)
    print("\n")
    print("original list {}".format(lst1))
    sorted_list = bubbleSort(lst1)
    print("sorted list {}".format(sorted_list))
    print("\n")
    merged_list = merging(lst1, lst2)
    print("mergelist {}".format(merged_list))
    print("\n")
    reversed_list = revrse(lst2)
    print("reversed list {}".format(reversed_list))


main()
