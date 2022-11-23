# Быстрая сортировка
array = [15, 10, 5, 6, 14, 12, 19, 4]

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        elem = array[0]
        left = [i for i in array if i < elem]
        equal = [i for i in array if i == elem]
        right = [i for i in array if i > elem]

        return quick_sort(left) + equal + quick_sort(right)


print(quick_sort(array))