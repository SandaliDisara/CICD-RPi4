def calculate_total_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Example usage:
numbers = [10, 20, 30, 40, 50]
total, average = calculate_total_and_average(numbers)
print("Total:", total)
print("Average:", average)
