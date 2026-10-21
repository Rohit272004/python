a = [1, 2]
a.append([3, 4])
print(a)
# [1, 2, [3, 4]]

a.extend([3,4])
print(a)

nums =[100,28,23,45]
print(sorted(nums)) #only returns the sorted list the original list is not changed
print(nums)

print(a.count(3))
print(a.index(3))