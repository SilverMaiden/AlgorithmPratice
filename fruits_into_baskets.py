def fruits_into_baskets(fruits):
  # TODO: Write your code here
  window_start = 0

  max_baskets = 2
  used_baskets = 0
  total_fruit = 0

  char_map = {}

  for window_end in range(len(fruits)):
    # Step 1: If used_baskets == 2, then we need to get rid of the key/val
    # pairing of window_start then increase window_start by 1,
    # moving the sliding window along
    if used_baskets == max_baskets:
      if fruits[window_end] not in char_map:
        del(char_map[fruits[window_start]])
        print(char_map)
        window_start += 1
        used_baskets -= 1

    # Step 2.1: If the current char is not in char_map, we need to add it along
    # with increase the value of used_baskets
    if fruits[window_end] not in char_map:
      char_map[fruits[window_end]] = 1
      used_baskets += 1
    # Step 2.2: If the current char is in char_map, we need to add it along
    # without increasing the value of used_baskets
    else:
      char_map[fruits[window_end]] += 1
  # Step 3: Add together all the values in char_map to get the total
  # num of fruits
  for each in list(char_map.values()):
    total_fruit += each

  return total_fruit

