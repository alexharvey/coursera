largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
        
    try:
        num = int(num)
    except ValueError:
        print 'Invalid input'
        continue
    
    if largest == None:
        largest = num
    elif num > largest:
        largest = num
        
    if smallest == None:
        smallest = num
    elif num < smallest:
        smallest = num

print "Maximum", largest
print 'Minimum', smallest