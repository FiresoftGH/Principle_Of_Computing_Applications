# Reference: https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm

def insertion_sort(array):
   for i in range(1, len(array)):
      j = i - 1
      next_element = array[i]

   while array[j] > next_element and j >= 0:
      array[j + 1] = array[j]
      j = j - 1

   array[j + 1] = next_element

array_1 = [19,2,31,45,30,11,121,27]
insertion_sort(array_1)
print(array_1)

def bubblesort(array):
   for iterate_number in range(len(array) - 1, 0, -1):
      for index in range(iterate_number):
         if array[index] > array[index + 1]:
            temp = array[index]
            array[index] = array[index + 1]
            array[index + 1] = temp

array_2 = [4, 42, 85, 50, 72, 75, 83, 94, 33, 7]
bubblesort(array_2)
print(array_2)

def merge_sort(array):
   if len(array) <= 1:
      return array

   middle = len(array) // 2
   left_list = array[:middle]
   right_list = array[middle:]
   return list(merge(left_list, right_list))

# Merge the two halves
def merge(left_half, right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])

      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])

      if len(left_half) == 0:
         res = res + right_half
      else:
         res = res + left_half
      return res

array_3 = [55, 91, 12, 43, 7, 53, 96, 83, 57, 17]
merge_sort(array_3)
print(array_3)

# def shell_sort(array):
#    gap = len(array) // 2
#    while gap > 0:
#       for i in range(gap, len(array)):
#          temp = array
#          j = i
#
#    while j >= gap and array[j - gap] > temp:
#       array[j] = array[j - gap]
#       j = j - gap
#       array[j] = temp
#
#    gap = gap // 2
#
# array_4 = [27, 73, 56, 45, 3, 37, 42, 69, 86, 42]
# shell_sort(array_4)
# print(array_4)

def selection_sort(array):
   for index in range(len(array)):
      minimum_index = index
      for j in range(index + 1, len(array)):
         if array[minimum_index] > array[j]:
            minimum_index = j

   array[index], array[minimum_index] = array[minimum_index], array[index]

array_5 = [36, 60, 84, 27, 73, 79, 0, 1, 54, 24]
selection_sort(array_5)
print(array_5)


