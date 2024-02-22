from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Drop microseconds
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print the result
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", current_datetime_without_microseconds)
