# Write a script in python or javascript to find the solution of the following problem
# How many two or more digit numbers can you make such that digits on left are always smaller than the digits on the right in the number

count=0
for first in range(1,10):
  for second in range(first+1, 10):
    count+=1
    for third in range(second+1,10):
      number=int(str(first) + str(second) + str(third))
      #print(number)

print(count)