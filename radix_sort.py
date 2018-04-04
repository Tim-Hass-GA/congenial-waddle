# RADIX SORT

my_list = [37,4,56,212,25,81,39,6,88,50,90,131,88,41,37,4,56,2,5,81,89,62,80,78,5,92,31,818,41]
my_list_b = [37,4,56,212,25,81,39,6,88,50,90,131,88,41,37,4,56,2,5,81,89,62,80,78,5,92,31,818,41]
my_list_c = [37,4,56,212,25,81,39,6,88,50,90,131,88,41,37,4,56,2,5,81,89,62,80,78,5,92,31,818,41]

################
# https://en.wikipedia.org/wiki/Radix_sort
################
def radix_sort(a_list, base=10):
  def list_to_buckets(a_list, base, iteration):
    buckets = [[] for _ in range(base)]
    for number in a_list:
      # print(number)
      # isolate the base-digit from the number
      digit = (number // (base ** iteration)) % base
      # drop the number into the correct bucket
      buckets[digit].append(number)
    return buckets

  def buckets_to_list(buckets):
    numbers = []
    for bucket in buckets:
      # print(bucket)
      # append the numbers in a bucket
      for number in bucket:
        numbers.append(number)
    return numbers

  maxval = max(a_list)
  it = 0
  # iterate, sorting the a_list by each base digit
  while base ** it <= maxval:
    a_list = buckets_to_list(list_to_buckets(a_list, base, it))
    it += 1
    # print(it)
  return a_list




print('my_list is',my_list)
print('output')
print(radix_sort(my_list))

################
# http://www.geekviewpoint.com/python/sorting/radixsort
################
def radix_sort_damier(aList):
  RADIX = 10
  maxLength = False
  tmp, placement = -1,1

  while not maxLength:
    maxLength = True
    # decalre an initialize buckets
    buckets = [list() for _ in range(RADIX)]
    # split aList between lists
    for i in aList:
      # print(i)
      tmp = i // placement
      # print(tmp)
      buckets[tmp % RADIX].append(i)
      if maxLength and tmp > 0:
        maxLength = False

    a = 0
    for b in range(RADIX):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    placement *= RADIX
  return aList




print('my_list is',my_list_b)
print('output')
print(radix_sort_damier(my_list_b))

################
# https://www.geeksforgeeks.org/radix-sort/
### counting sort
################
def counting_sort_g4g(a_list, expl):
  # print(a_list)
  n = len(a_list)
  # output list of sorted elements
  output = [0] * (n)
  # initialize count list at 0
  count = [0] * (10)
  #store occurance of count
  for i in range(0,n):
    index = (a_list[i]//expl)
    count[ (index)%10 ] += 1
  # change count[i] to actual position
  for i in range(1,10):
    count[i] += count[i-1]
  # build output list
  i = n-1
  while i >= 0:
    index = (a_list[i]//expl)
    output[ count[ (index)%10 ] - 1 ] = a_list[i]
    count [ (index)%10 ] -= 1
    i -= 1
  #copy output list to list
  i = 0
  for i in range(0, len(a_list)):
    a_list[i] = output[i]

################
## radix_sort (USES COUNTING SORT)
################
def radix_sort_g4g(a_list):
  # find max number
  max1 = max(a_list)
  # do counting sort
  exp = 1
  while max1//exp > 0:
    counting_sort_g4g(a_list,exp)
    exp *= 10
  return a_list




print('my_list is',my_list_c)
print('output')
print(radix_sort_g4g(my_list_c))
