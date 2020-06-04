sum=0
count=0
print("Before sum and count:",sum,count)
for thing in [2,34,5,41,17,1,62]:
    count+=1
    sum+=thing
    print(count,thing,sum)
print("count is",count)
print("csum is",sum)
print("average is",sum/count)
