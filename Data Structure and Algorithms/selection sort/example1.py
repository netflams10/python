## Remeber 0(n) <--> searches each element through the whole list
## Sort an array from smaller to largest

def findSmallest (arr):
    ## store the smallest value
    smallest = arr[0]

    ## Store index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


## Nowwrite the array for the selection sort
def selectionSort (arr):
    newArr = []
    for i in range(len(arr)):
        ## find smallest element in the arrar, and add it to the new array
        smallest = findSmallest(arr)
        # print(smallest)
        newArr.append(arr.pop(smallest))
        # print(arr)
    return newArr


print (selectionSort([5, 6, 3, 1, 0]))
# print (findSmallest([5, 6, 3, 1, 0]))