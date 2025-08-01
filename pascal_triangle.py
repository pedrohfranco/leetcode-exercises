def generate(self, numRows):
  """
  :type numRows: int
  :rtype: List[List[int]]
  """

  triangle = [[1], ]
  for i in range(1, numRows):
    triangle.append([1])
    for j in range(1, i):
      triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
    triangle[i].append(1)
  
  return triangle

print(generate(None, 5))