def bogosort(array):
  if is_sorted(array):
    return array
  else:
    shuffle(array)
    return bogosort(array)

def is_sorted(array):
  for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
      return False
  return True

def shuffle(array):
  for i in range(len(array)):
    j = random.randint(0, len(array) - 1)
    array[i], array[j] = array[j], array[i]
