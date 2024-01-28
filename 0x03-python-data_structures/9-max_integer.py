#!/usr/bin/python3

def max_integer(my_list=[]):
  """Finds the biggest integer in a list without using max() or imports, handling empty lists.

  Args:
    my_list: The input list of integers.

  Returns:
    The biggest integer in the list, or None if the list is empty.
  """

  if not my_list:
    return None  # Handle empty list

  biggest_num = my_list[0]  # Start with the first element as the biggest
  for num in my_list:
    if num > biggest_num:
      biggest_num = num  # Update if a larger number is found

  return biggest_num
