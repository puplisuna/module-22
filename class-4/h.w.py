x = int(input("Enter a number: "))
n = int(input("Enter the exponent: "))
print(" power series is: ")
for i in range(1, n + 1):
    print(x** i, end=" ")
print("\nThe sum of the series is: ", sum(x** i for i in range(1, n + 1)))
print("The product of the series is: ", eval('*'.join(str(x** i) for i in range(1, n + 1))))
print("The average of the series is: ", sum(x** i for i in range(1, n + 1)) / n)
print("The maximum of the series is: ", max(x** i for i in range(1, n + 1)))
print("The minimum of the series is: ", min(x** i for i in range(1, n + 1)))