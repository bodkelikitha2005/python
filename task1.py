# 1. Sum of two numbers – take input & print their sum
def sum_two_numbers():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    result = x + y
    print("Sum =", result)

# 2. Odd or even checker – check if a number is odd/even
def odd_or_even():
    n = int(input("Enter an integer: "))
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

# 3. Factorial calculation – using a loop or recursion
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
def factorial_program():
    n = int(input("Enter a non-negative integer for factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("Factorial (iterative) of", n, "=", factorial_iterative(n))
        print("Factorial (recursive) of", n, "=", factorial_recursive(n))

# 4. Fibonacci sequence – Generate first n numbers
def fibonacci_sequence():
    n = int(input("Enter how many Fibonacci numbers to generate: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print("First", n, "Fibonacci numbers:", sequence)

# 5. String reverse – reverse user-input string
def reverse_string():
    s = input("Enter a string to reverse: ")
    reversed_s = s[::-1]
    print("Reversed string:", reversed_s)

# 6. Palindrome checker – is the word same forward and backward
def palindrome_checker():
    s = input("Enter a word/string to check palindrome: ")
    if s == s[::-1]:
        print(s, "is a palindrome")
    else:
        print(s, "is not a palindrome")

# 7. Leap year check – check if a given year is leap year
def leap_year_check():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

# 8. Armstrong number – check if a number is an Armstrong number
def armstrong_check():
    num = int(input("Enter a positive integer: "))
    num_str = str(num)
    n = len(num_str)
    sum_of_powers = sum(int(digit) ** n for digit in num_str)
    if sum_of_powers == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


def main():
    while True:
        print("\nChoose one of the programs:")
        print("1: Sum of two numbers")
        print("2: Odd or even checker")
        print("3: Factorial calculation")
        print("4: Fibonacci sequence")
        print("5: String reverse")
        print("6: Palindrome checker")
        print("7: Leap year check")
        print("8: Armstrong number check")
        print("9: Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            sum_two_numbers()
        elif choice == '2':
            odd_or_even()
        elif choice == '3':
            factorial_program()
        elif choice == '4':
            fibonacci_sequence()
        elif choice == '5':
            reverse_string()
        elif choice == '6':
            palindrome_checker()
        elif choice == '7':
            leap_year_check()
        elif choice == '8':
            armstrong_check()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a valid option (1-9).")

if __name__ == "__main__":
    main()
