def check_and_change_list(x):
    p = x.split()
    list_ = []
    for i in p:
        try:
            i = int(i)
        except ValueError:
             return print("Допускаются только числа")
        else:
            list_.append(i)

    return list_

def sort_list(a):
    list_ = check_and_change_list(a)
    if type(list_) != list:
        return
    N = len(list_)
    for i in range(0, N-1):
        for j in range(0, N-1-i):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_

def binary_search(array, element, left, right):
    if left > right or type(array) != list:
        return False
    middle = (left + right) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)

def len_list(x):
    list_ = len(check_and_change_list(x))
    return list_-1



inter =  input("Введите числа через пробел: ")
element = int(input("Введите число: "))
list_ = binary_search(sort_list(inter), element, 0, len_list(inter))


print(list_)

