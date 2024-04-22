pattern_number = int(input("Enter pattern number: "))

for i in range(1, pattern_number+1, 1):
    for j in range(1, i+1, 1):
        print(j, end="")
    print()
