import matplotlib.pyplot as plt
import csv

# Read the generation data from CSV
time = []
generation = []

with open('generation_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if present
    for row in reader:
        time.append(float(row[0]))  # Assuming time values are in the first column
        generation.append(float(row[1]))  # Assuming generation values are in the second column

# Create the line plot
plt.plot(time, generation, marker='o', linestyle='-', color='b')

# Set the labels and title
plt.xlabel('Time (hours)')
plt.ylabel('Power Generation (kW)')
plt.title('Solar Power Plant Generation')

# Show the plot
plt.show()
