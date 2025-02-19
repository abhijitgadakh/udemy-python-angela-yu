
import math


def check_prime(number):
    counter = 2
    is_prime = True

    while(num > counter):
        if num % counter == 0:
            is_prime = False
        
        counter += 1
    
    if(is_prime):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a not prime number")


num = int(input("Enter number you want to check for prime: "))

check_prime(num)