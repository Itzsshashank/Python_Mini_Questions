def fizz_buzz():
    length = int(input("Enter Length: "))
    for num in range(1, length):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
          
fizz_buzz()

# In this Python program, the fizz_buzz() function iterates through numbers from 1 till the lenght entered by user, using a loop. It checks the divisibility of each number by 3 and 5 and prints the appropriate output accordingly.
