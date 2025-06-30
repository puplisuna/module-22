def is_natural_number(n):
   
    if isinstance(n, int) and n > 0:
        return True
    else:
        return False
    


    

try:
    num = int(input("Enter a number: "))
    if is_natural_number(num):
        print(f"{num} is a natural number.")
    else:
        print(f"{num} is NOT a natural number.")
except ValueError:
    print("Invalid input. Please enter an integer.")