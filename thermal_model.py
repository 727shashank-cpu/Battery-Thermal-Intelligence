import numpy as np
import matplotlib.pyplot as plt

# Battery properties
mass = 0.070
specific_heat = 1000
resistance = 0.025

# Environmental properties
ambient_temperature = 25
h = 100
surface_area = 0.01

# Operating conditions
current = 5
initial_temperature = 25

# Simulation settings
time_step = 1
total_time = 4000

time_values = np.arange(0, total_time + time_step, time_step)

temperature = initial_temperature
temperature_values = []

# Heat generation
heat_generation = current**2 * resistance

# Time simulation
for t in time_values:

    # Heat removed by surroundings
    heat_loss = h * surface_area * (
        temperature - ambient_temperature
    )

    # Net heat generation
    net_heat = heat_generation - heat_loss

    # Temperature change
    temperature_change = (
        net_heat * time_step
        / (mass * specific_heat)
    )

    # Update temperature
    temperature = temperature + temperature_change

    temperature_values.append(temperature)

# Plot results
plt.plot(time_values, temperature_values)

plt.xlabel("Time (seconds)")
plt.ylabel("Battery Temperature (°C)")
plt.title("Battery Temperature vs Time")

plt.grid()
plt.savefig(f"thermal_model_h{h}.png", dpi=200)
print(f"Graph saved for h = {h}")