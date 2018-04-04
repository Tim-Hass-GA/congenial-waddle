import math

my_list = [37,4,56,2,5,81,89,62,88,5,92,31,88,41]

def bucket_sort(bucket_list, bucket_count):
  if len(bucket_list) == 0:
    return bucket_list
    #organize in buckets
    #sort those buckets
    #drop into the appropriate spot
  minValue = bucket_list[0]
  maxValue = bucket_list[0]
  for x in range(1, len(bucket_list)):
    if bucket_list[x] < minValue:
      minValue = bucket_list[x]
    elif bucket_list[x] > maxValue:
      maxValue = bucket_list[x]
  print(maxValue)
  print(minValue)

  buckets = []
  for y in range(0, bucket_count +1):
    buckets.append([])

  bucket_size = math.floor((maxValue - minValue)/ bucket_count)
  print(bucket_size)

  # distribute  input list value into buckets
  for i in range(0, len(bucket_list)):
    buckets[math.floor(bucket_list[i]/ bucket_size)].append(bucket_list[i])
  print(buckets)

  for x in range(len(buckets)):
    print(buckets[x])
    if len(buckets[x]) > 1:
      for j in range(0, len(buckets[x])-1):
        if buckets[x][j] > buckets[x][j+1]:
          temp = buckets[x][j]
          buckets[x][j] = buckets[x][j+1]
          buckets[x][j+1] = temp
  print("buckets",buckets)

  flat_list = list()
  for bucket in buckets:
    for item in bucket:
      flat_list.append(item)
  return flat_list




print('parmas my_list, 6', my_list)
print('output')
print(bucket_sort(my_list, 6))
