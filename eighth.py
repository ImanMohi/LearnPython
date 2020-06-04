#usage of data type NONE
smallest = None
print('before')
for value in [9,41,12,13,74,15,1]:
    if smallest is None :              #here 'IS' is an operator
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after',smallest)
