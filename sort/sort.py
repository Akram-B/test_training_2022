# inspired by https://realpython.com/sorting-algorithms-python/#pythons-built-in-sorting-algorithm
import timeit
import random


def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


from random import randint


def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


def generate_random_array(size):
    return [random.randint(1, 10_000) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(1, size + 1))


def generate_sorted_array_with_min_at_end(size):
    return list(range(2, size + 1)) + [1]


def generate_reversed_sorted_array(size):
    return list(range(size, 0, -1))


def generate_reversed_sorted_array_with_max_at_end(size):
    return list(range(size - 1, 0, -1)) + [size]


def measure_performance(test_case, sorting_algorithm):
    time_taken = timeit.timeit(lambda: sorting_algorithm(test_case.copy()), number=1)
    return time_taken


# Define the size of the arrays
array_size = 10_000

# Generate test cases
random_array = generate_random_array(array_size)
sorted_array = generate_sorted_array(array_size)
sorted_array_with_min_at_end = generate_sorted_array_with_min_at_end(array_size)
reversed_sorted_array = generate_reversed_sorted_array(array_size)
reversed_sorted_array_with_max_at_end = generate_reversed_sorted_array_with_max_at_end(array_size)

sorting_algorithms = [quicksort, merge_sort, bubble_sort, insertion_sort, list.sort]

# Generate test cases
test_cases = {
    "Random Array": generate_random_array(array_size),
    "Sorted Array": generate_sorted_array(array_size),
    "Sorted Array with Min at End": generate_sorted_array_with_min_at_end(array_size),
    "Reversed Sorted Array": generate_reversed_sorted_array(array_size),
    "Reversed Sorted Array with Max at End": generate_reversed_sorted_array_with_max_at_end(array_size)
}

# Dictionary to store the best algorithm for each test case
best_algorithms = {test_case_name: None for test_case_name in test_cases}

# Measure performance for each test case and each algorithm
for algorithm in sorting_algorithms:
    print(f"Performance for {algorithm.__name__}:")
    for test_case_name, test_case in test_cases.items():
        execution_time = measure_performance(test_case, algorithm)
        print(f"{test_case_name} Sorting Time: {execution_time:.6f} seconds")

        # Update the best algorithm for each test case
        if best_algorithms[test_case_name] is None or execution_time < best_algorithms[test_case_name][1]:
            best_algorithms[test_case_name] = (algorithm.__name__, execution_time)

    print()  # Separate results for different algorithms

# Print the best algorithm for each test case
print("Best Algorithms:")
for test_case_name, (best_algorithm, best_time) in best_algorithms.items():
    print(f"{test_case_name}: {best_algorithm} (Time: {best_time:.6f} seconds)")
