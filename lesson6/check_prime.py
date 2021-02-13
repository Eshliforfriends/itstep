error = "Input a digit"
prime = "Your number is prime"
not_prime = "Your number is not prime"
try:
    user_number = int(input("Please enter a number: "))
    for i in range(2, user_number):
        if user_number % i == 0:
            print(not_prime)
            break
    else:
        print(prime)
except:
    print(error)