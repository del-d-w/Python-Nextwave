# Function to parse a time string in the format "X hr Y min" and return total minutes
def parse_time(time_str):
    parts = time_str.split()
    total_minutes = 0
    for i in range(len(parts)):
        if parts[i] == 'hr':
            total_minutes += int(parts[i - 1]) * 60
        elif parts[i] == 'min':
            total_minutes += int(parts[i - 1])
    return total_minutes

# List of times in the format "X hr Y min"
times = [
    "1 hr 35 min", "1 hr 49 min", "1 hr 51 min",
    "1 hr 14 min", "1 hr 14 min", "3 hr 43 min",
    "2 hr 39 min", "1 hr 43 min", "1 hr 26 min",
    "2 hr 34 min", "0 hr 58 min", "1 hr 6 min",
    "0 hr 42 min", "4 hr 46 min", "1 hr 31 min",
    "1 hr 29 min", "1 hr 38 min", "0 hr 51 min",
    "2 hr 0 min", "3 hr 35 min", "0 hr 43 min",
    "0 hr 55 min", "1 hr 49 min", "1 hr 29 min",
]

# Initialize total hours and minutes
total_hours = 0
total_minutes = 0

# Calculate the total hours and minutes
for time_str in times:
    minutes = parse_time(time_str)
    total_minutes += minutes

# Convert total minutes to hours and minutes
total_hours = total_minutes // 60
remaining_minutes = total_minutes % 60

# Display the result
print(f"Total Time: {total_hours} hr {remaining_minutes} min")
