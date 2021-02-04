def find_averages_of_subarrays(K, arr):

  result = []

  windowSum, windowStart = 0.0, 0

  for windowEnd in range(len(arr)):
    # Step 1: Keep adding windowEnd to windowSum until we get to length K
    windowSum += arr[windowEnd]
    # Step 2: Once we've reached length K or K-1, we want to store the average
    if windowEnd >= K - 1:
      sub_arr_avg = windowSum / K
      result.append(sub_arr_avg)
      #Step 3: After storing the average, we need to take away arr[windowStart] from
      # windowSum as the sliding window moves one element forward
      windowSum = windowSum - arr[windowStart]
      # The sliding window needs to move one element forward,
      # so we increase windowStart by 1
      windowStart += 1
  return result





def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()

