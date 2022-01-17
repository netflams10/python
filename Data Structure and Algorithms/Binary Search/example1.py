# low = 0
# high = len(list) -1 # list starts at 0

# Getting the mid item
# mid = (low + high) / 2
# guess = list[mid]

# if guess is low update low
# if guess < item:
#     low = mid + 1

def binary_search (list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist = [1, 3, 5, 8, 9, 10]

# print(binary_search(mylist, 3))
# print(binary_search(mylist, -1))

#  Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

# max_number_of_names = 128
# worst_case = 0

# while max_number_of_names > 0:
#     print(max_number_of_names)
#     worst_case += 1
#     max_number_of_names //= 2

## At this hour i don't know if there any better soln which i believe there are but i did this on my own...
## So please you can try yours and share ...

def calculate_maximum_search(length_of_list, worst_time = 0):
    if (length_of_list <= 0):
        return worst_time;
    return calculate_maximum_search(length_of_list // 2, worst_time + 1)


print(calculate_maximum_search(128))