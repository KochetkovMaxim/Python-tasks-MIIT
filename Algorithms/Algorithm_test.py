import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 100000
NUMBER_OF_TESTS = 10
RAND_MAX = 100000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_

def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True

def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")

def quick_sort(array):
    sorted_array = array.copy()
    if len(sorted_array) <= 1:
        return sorted_array
    elif len(sorted_array) == 2 and sorted_array[0] > sorted_array[1]:
        sorted_array[0], sorted_array[1] = sorted_array[1], sorted_array[0]
        return sorted_array
    else:
        element = sorted_array[0]
        left = []
        equal = []
        right = []
        for i in sorted_array:
            if i > element:
                right.append(i)
            elif i < element:
                left.append(i)
            else:
                equal.append(i)

        return quick_sort(left) + equal + quick_sort(right)
  