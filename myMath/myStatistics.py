  
''' myStatistics '''
def myMean( A):
  sum = 0
  N = 0
  for i in A:
    sum += i
    N += 1
  if N > 0:
    return sum/N
  if N == 0:
    return False

def myMax(A):
  max = 0
  for i in A:
    if i > max:
      max = i
  return max
  
def myMin(A):
  min = 0
  for i in A:
    if i < min:
      min = i
  return min