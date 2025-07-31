def subarrayBitwiseORs(self, arr):
  """
  :type arr: List[int]
  :rtype: int
  """

  result = set()
  actual = set()

  for x in arr:
    _next = {x | y for y in actual}
    _next.add(x)

    result.update(_next)
    actual = _next
  
  return len(result)

print(subarrayBitwiseORs(None, [39,19,30,56,79,50,19,70,30]))