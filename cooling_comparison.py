import numpy as np
import matplotlib.pyplot as plt

# Battery properties
mass = 0.070
specific_heat = 1000
resistance = 0.025
ambient_temperature = 25
surface_area = 0.01
current = 5

# Simulation settings
initial_temperature = 25
time_step = 1
total_time = 4000

time_values = np.arange(0, total_time + time_step, time_step)

# Cooling conditions
h_values = [5, 10, 30, 50, 100]

# Simulate each cooling condition
for h in h_values:

    temperature = initial_temperature
    temperature_values = [initial_temperature]

    heat_generation = current**2 * resistance

    for t in time_values[1:]:

        heat_loss = h * surface_area * (
            temperature - ambient_temperature
        )

        net_heat = heat_generation - heat_loss

        temperature_change = (
            net_heat * time_step
            / (mass * specific_heat)
        )

        temperature += temperature_change

        temperature_values.append(temperature)

    plt.plot(
        time_values,
        temperature_values,
        label=f"h = {h}"
    )

# Graph formatting
plt.xlabel("Time (seconds)")
plt.ylabel("Battery Temperature (°C)")
plt.title("Battery Cooling Comparison")
plt.legend()
plt.grid()

plt.savefig("cooling_comparison.png", dpi=200)

print("Comparison graph saved successfully!")