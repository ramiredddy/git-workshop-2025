# Program to check if a number is even or odd

def check_even_odd(number):
    """
    Check if a number is even or odd.
    
    Args:
        number (int): The number to check
    
    Returns:
        str: 'even' if the number is even, 'odd' if the number is odd
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    # Test the function
    test_number = int(input("Enter a number: "))
    result = check_even_odd(test_number)
    print(f"The number {test_number} is {result}.")
