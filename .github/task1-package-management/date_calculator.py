from datetime import datetime

def date_difference(date1, date2):
    """
    Calculates the number of days between two dates (in 'YYYY-MM-DD' format).
    """
    try:
        # Convert strings to datetime objects
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        # Return absolute difference in days
        return abs((d2 - d1).days)
    except ValueError:
        print("Please use the correct date format: YYYY-MM-DD")

# Example usage
print(date_difference("2024-01-01", "2024-01-10"))  # Output: 9