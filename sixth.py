largest_so_far = -1
print("before: ",largest_so_far)
for i in [9,3,12,41,34,56,74,2,31]:
    if i > largest_so_far:
        largest_so_far = i
    print (largest_so_far,i)

print("After:",largest_so_far)
