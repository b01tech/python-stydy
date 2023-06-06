

def prime_number_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("It is a Prime Number!")
    else:
        print("It is NOT a Prime Number!")


num = int(input("Chose a number to check: "))
prime_number_checker(num)
