
def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  current_shortest_sub_arr = len(arr)
  window_sum, window_start = 0.0, 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
      # In this case, we want to count the length of the current sub array
      # We can do this by taking away window_start from window_end
      sub_arr_length = (window_end - window_start) + 1
      current_shortest_sub_arr = min(current_shortest_sub_arr, sub_arr_length)
      #Take away arr[window_start] from window_sum
      window_sum -= arr[window_start]
      #increase window start by 1 to move sliding window forward
      window_start += 1

  return current_shortest_sub_arr
