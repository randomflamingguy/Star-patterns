print("Star pattern \n")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print('\n')
print("Inverted Star pattern \n")
for i in range(6,1,-1):
    for j in range(i,1,-1):
        print("*", end="")
    print('\n')
    