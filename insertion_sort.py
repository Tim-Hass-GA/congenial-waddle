## insert sort
my_list = [1,3,5,6,2,4]

def selection_sort(a_list):
  n = len(a_list)
  for x in range(0,n):
    key = a_list[x]
    j = x - 1
    while j >= 0 and key < a_list[j]:
      a_list[j+1] = a_list[j]
      j -= 1
    a_list[j+1] = key
  return a_list

print('my_list is',my_list)
print('output')
print(selection_sort(my_list))
