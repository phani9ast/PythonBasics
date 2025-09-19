def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(int(n/2),2,-1):
        if n%i==0:
            print(i)
            return False            
    return True
    
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
    
    

    """# Check divisibility from 3 up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_even(n):
    if n%2==0:
        return True

# Main program
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

if is_even(num):
    print (f"{num} is Even")
else:
    print (f"{num} is Odd")"""