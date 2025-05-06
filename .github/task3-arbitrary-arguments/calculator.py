def calculate(*numbers, add=False, subtract=False, multiply=False, divide=False):
    """
    Performs basic arithmetic operations on numbers.
    Only one operation should be set to True.
    """
    if not numbers:
        return "No numbers provided."

    result = numbers[0]
    others = numbers[1:]

    if add:
        result = sum(numbers)
    elif subtract:
        for num in others:
            result -= num
    elif multiply:
        for num in others:
            result *= num
    elif divide:
        for num in others:
            if num == 0:
                return "Error: Cannot divide by zero."
            result /= num
    else:
        return "No valid operation selected."

    return result

# Example usage
if __name__ == "__main__":
    print(calculate(10, 5, add=True))       # Output: 15
    print(calculate(10, 2, multiply=True))  # Output: 20
