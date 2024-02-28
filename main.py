def average(array):
  num = len(array)
  if num == 1:
    return array[0]
  else:
    return (array[0] + average(array[1:]) * (num-1))/num

array = [1,2,3,4,5,6]
print(average(array))
