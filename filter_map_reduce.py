from functools import reduce



nums = {3,4,1,5,65,2,2,6,3}

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(lambda a,b : a+b, doubles)
print(sum)
print(evens)

print(doubles)
