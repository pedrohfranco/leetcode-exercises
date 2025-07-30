def longestSubarray(self, nums):
  """
  :type nums: List[int]
  :rtype: int
  """

  _max = max(nums)
  longest_size = 1
  count = 0
  for num in nums:
    if num == _max: count += 1
    else: count = 0
    longest_size = max(longest_size, count)
  return longest_size

print(longestSubarray(None, [1, 2, 4, 4]))

def longestSubarray2(self, nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  k = nums[0]
  count = 0
  max_count = 0
  for num in nums:
    if num == k: count += 1
    if num > k: 
      k = num
      max_count = 1
      count = 1
    if num < k:
      max_count = max(max_count, count)
      count = 0
  max_count = max(max_count, count)
  return max_count


print(longestSubarray2(None, [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]))

    

