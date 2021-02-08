def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here

  #Step 1: Start with basic sliding window approach
  window_str, window_start = "", 0
  current_longest_substr_len = 0

  for window_end in range(len(str)):
    window_str += str[window_end]
    print(window_str)

    # Get current number of distinct chars in window_str
    distinct_chars = set(window_str)
    print(len(distinct_chars))
    print(distinct_chars)

    #This while loop takes place when we have more than
    #k distinct chars in the str
    while len(set(window_str)) > k and (window_start < window_end - 1):
      substr_len = len(window_str)
      # Cutting off end character to avoid going over limit
      # Since this loop starts when we have more than
      # k distinct chars in the str, we need to go back one element
      cut_window_str = str[window_start : window_end]
      cut_substr_len = len(cut_window_str)

      # Compare current longest substr len with cut_substr_len, replace
      # if new val is longer
      current_longest_substr_len = max(current_longest_substr_len, cut_substr_len)

      # increase window_start by 1 if it's still before window_end
      window_start += 1
      window_str = str[window_start: window_end]


  (print("THE END REACHED ", current_longest_substr_len))
  return current_longest_substr_len
