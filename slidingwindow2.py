#Problem Statement #
#Given an array of positive numbers and a positive number ‘k,’
#find the maximum sum of any contiguous subarray of size ‘k’.

#Time Complexity: O(n)
#Space Complexity: O(1)

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  window_sum, window_start = 0.0, 0
  current_max = 0
  #No need to store in a results array, just track current max
  #results = []
  for window_end in range(len(arr)):
    window_sum += arr[window_end]

    #Once we've reached length K or K-1, we want to store the average
    if window_end >= k - 1:
      current_max = max(current_max, window_sum)
      window_sum -= arr[window_start]
      window_start += 1

  return current_max

def main():
  result1 = max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
  result2 = max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
  print("result1: max sub array of size K: " + str(result1))
  print("result2: max sub array of size K: " + str(result2))


main()

