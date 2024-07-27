from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Format the date and time
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_now}")

# Calculate a date 10 days from now
future_date = now + timedelta(days=10)
print(f"Date 10 days from now: {future_date}")

# Parse a date string
date_string = "2024-07-01"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")
