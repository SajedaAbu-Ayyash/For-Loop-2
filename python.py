# 1.Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#     return list
# print(biggie_size([-1,3,5,-5]))

def biggie_size():
    my_list = [-1, 3, 5, -5]
    for i in range(0, len(my_list), 1):
        if (my_list[i] > 0):
            my_list[i] = "Big"

    print(my_list)
   
# 2.Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positive():
    my_list = [-1,1,1,1]
    for i in range(0, len(my_list), 1):
        if(my_list[i] > 0):
            my_list[i] += 2
            
    print(my_list)

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total():
    my_list = [1,2,3,4]
    sum = 0
    for i in range(0, len(my_list), 1):
        sum = sum + my_list[i]

    print(sum)

# 4. Average - Create a function that takes a list and returns the average of all the values.x
def average():
    my_list = [1,2,3,4]
    for i in range(len(my_list)):
     total = sum(my_list)
    return (total / len(my_list))
result = average()
print(result)

# 5. Length - Create a function that takes a list and returns the length of the list.
# def length():
#     my_list = [37,2,1,-9]
#     for i in range(0, len(my_list), 1):
#      return len(my_list)
# result = length()
# print(result)

def length(list):
   return len(list)
print(length([37,2,1,-9]))
print(length([]))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum():
   my_list = [37,2,1,-9]
   for i in range(0, len(my_list), 1):
      if (my_list[i] > 0):
       return min
      elif (my_list[i] == None):
         return False
   result = minimum()
   print(result)

# 7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum():
   my_list = [37,2,1,-9]
   max_num = 0
   for i in my_list:
      if i > max_num:
         max_num = i
   print(max_num)

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis():
   my_list = [37,2,1,-9]
   dictionary = {
      'sumTotal' : sum(my_list),
      'average' : sum(my_list) / len(my_list),
      'minimum' : min(my_list),
      'maximum' : max(my_list),
      'length' : len(my_list)
   }
   for i in my_list:
      if dictionary['minimum'] < i:
         dictionary['minimum'] = i
      elif dictionary['maximum'] > i:
         dictionary['maximum'] = i

      dictionary['sumTotal'] += i
      dictionary['average'] = dictionary['sumTotal'] / len(my_list)
      return dictionary
   print(ultimate_analysis())

# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)   
def reverse(my_list):
      a = 0
      mid = len(my_list) / 2
      for i in range(len(my_list)-1, int (mid), -1):
         temp = my_list[a]
         my_list[a] = my_list [i]
         my_list[i] = temp
         a += 1
      print(my_list)
reverse([37,2,1,-9])
