from datetime import datetime

# Define the two dates
date1 = datetime(2024, 2, 10, 12, 0, 0)  # First date
date2 = datetime(2024, 2, 5, 8, 30, 0)   # Second date

# Calculate the difference
difference = date1 - date2

# Convert the difference to seconds
difference_in_seconds = difference.total_seconds()

# Print the result
print("Difference in seconds:", difference_in_seconds)
