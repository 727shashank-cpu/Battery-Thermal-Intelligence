#Till now we saw, how temperature changes take place with time, current ahd h.
#Now we will see how temperature changes take place with dynamic current changes..

import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
time_step = 1
total_time = 1200

time_values = np.arange(
    0, total_time + time_step, time_step
)

# Define changing current over time
current_profile = np.zeros(len(time_values))

for i, t in enumerate(time_values):

    if t < 300:
        current_profile[i] = 2

    elif t < 600:
        current_profile[i] = 5

    elif t < 900:
        current_profile[i] = 1

    else:
        current_profile[i] = 4

# Plot current profile
plt.figure(figsize=(10, 5))

plt.plot(time_values, current_profile)

plt.xlabel("Time (seconds)")
plt.ylabel("Current (A)")
plt.title("Dynamic Battery Current Profile")

plt.grid(True)
plt.show()


# Battery properties
mass = 0.070
specific_heat = 1000
resistance = 0.025

ambient_temperature = 25
h = 10
surface_area = 0.01

initial_temperature = 25

# Temperature simulation
temperature = initial_temperature
temperature_history = [temperature]

for i in range(1, len(time_values)):

    current = current_profile[i]

    heat_generation = current**2 * resistance

    heat_loss = h * surface_area * (
        temperature - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat * time_step
        / (mass * specific_heat)
    )

    temperature = temperature + temperature_change

    temperature_history.append(temperature)

# Plot temperature response
plt.figure(figsize=(10, 5))

plt.plot(time_values, temperature_history)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Battery Temperature Under Dynamic Current")

plt.grid(True)
plt.savefig("Battery_Temperature_Under_Dynamic_Current.png", dpi=200)
plt.show()

# Print temperature at every current transition

for t in [299, 300, 301, 599, 600, 601,
          899, 900, 901, 1199, 1200]:

    index = int(t / time_step)

    print(
        f"Time: {t}s | "
        f"Current: {current_profile[index]} A | "
        f"Temperature: {temperature_history[index]:.4f} °C"
    )
    