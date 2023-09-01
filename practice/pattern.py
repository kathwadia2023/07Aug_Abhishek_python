#  pattern 1

for r in range(1,6):
    for c in range(r):
        print("*", end=" ")
    print(" ")    
# pattern 2

for r in range(1,6):
    for c in range(r):
        print(c+1, end=" ")
    print(" ")    

#  pattern 3

for r in range(6,0,-1):
    for c in range(r):
        print("*", end=" ")
    print(" ")    
