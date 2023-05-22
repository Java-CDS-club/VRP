import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Convert the string coordinates to tuples of floats
locations = [(float(coord.split(',')[0]), float(coord.split(',')[1])) for coord in [
    '11.16953,-4.28875',  # depot 0
    '11.16953,-3.99572',  #1
    '11.23405,-4.04314',  #2
    '11.27924,-3.98677',  #3
    '11.30249,-3.88924',  #4
    '11.33408,-3.91161',  #5
]]

# Extract the vehicle solution
solution = [
    {'vehicle': 0, 'route': [0, 3, 4, 5, 2, 0], 'distance': 107792},
    {'vehicle': 1, 'route': [0, 1, 0], 'distance': 65207},
]

fig, ax = plt.subplots(figsize=(10,10))

# Plot locations
for idx, location in enumerate(locations):
    ax.scatter(*location, label=str(idx))
    ax.text(location[0], location[1], f"{idx}", fontsize=12)

# Plot routes
for vehicle_solution in solution:
    route = vehicle_solution['route']
    coordinates = [locations[idx] for idx in route]
    for i in range(len(coordinates) - 1):
        p1, p2 = coordinates[i], coordinates[i+1]
        arrow = FancyArrowPatch(p1, p2, arrowstyle='->', mutation_scale=20, color='red')
        ax.add_patch(arrow)

plt.legend()
plt.grid(True)
plt.show()
