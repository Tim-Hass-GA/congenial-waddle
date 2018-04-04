## bubble sort
my_list = [1,3,5,6,2,4]

def bubble_sort(my_list):
  for x in range(len(my_list)):
    for y in range(0, len(my_list)-1):
      if my_list[y] > my_list[x]:
        my_list[y], my_list[x] = my_list[x], my_list[y]
      print(my_list)

bubble_sort(my_list)

########
# def bubbleSort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

######
# An optimized version of Bubble Sort
# def bubbleSort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         swapped = False
#         # Last i elements are already
#         #  in place
#         for j in range(0, n-i-1):
#             # traverse the array from 0 to
#             # n-i-1. Swap if the element
#             # found is greater than the
#             # next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         # IF no two elements were swapped
#         # by inner loop, then break
#         if swapped == False:
#             break




######
