"""Prime numbers are numbers that can only be cleanly divided by themselves and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4."""


user_input=int(input("Enter the number:"))

def prime_number(n):
    count=0
    for i in range(2,n):
        
        if n%i==0:
            count+=1
    if count==0:
        print("Prime Number")
    else:
        print("Not Prime Number")

prime_number(n=user_input)
