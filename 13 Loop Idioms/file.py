smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break #error is line 6, it break the loop before iterating all values
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)