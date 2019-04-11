def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError

   elif len(int_list) == 0:
      return None

   tempmax = int_list[0]
   for i in range(1,len(int_list)):
      if tempmax < int_list[i]:
         tempmax = int_list[i]
   return tempmax

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
  
   else:
      if len(int_list) == 0:
         return []
      return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError

   else:
      if len(int_list) == 0:
         return None
      idx = (high+low)//2
      if int_list[idx] == target:
         return idx
      elif int_list[idx] >= target and int_list[low] <= target:
         return bin_search(target, low, idx, int_list)
      elif int_list[idx] < target and int_list[high] >= target:
         return bin_search(target, idx + 1, high, int_list)
      else:
         return None
         
