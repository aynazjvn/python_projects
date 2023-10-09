def prime_checker(number):
    is_a_prime = True
    for integer in range(2,number):
        if number%integer == 0:
            is_a_prime = False
    if is_a_prime:
        print("It's a prime")
    else:
         print("It's not a prime")
                
        
            

n = int(input("Check this number :"))
prime_checker(number=n)    