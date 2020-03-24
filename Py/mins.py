def make_chocolate(small, big, goal):
  rem = goal
  smallCount = 0
  while big > 0 and rem > 0:
    rem -= 5
    big -= 1
  while rem > 0:
    rem -= 1
    small -= 1
    smallCount += 1
    if small < 0:
      return -1
  return smallCount
    
  
print(make_chocolate(1000, 1000000, 5000006))