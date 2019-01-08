#print("iam trying how to use github")
#print("iam try to add content from my meachine")
#7. Write the higher order function reduce to calculate the total sum of first 30 odd values in the range of 1 to 100. 

import functools
res = list(filter(lambda x: x % 2 == 1, list(range(0, 101))))
print(res)
res = functools.reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 1, range(1, 100)))
print(res)


