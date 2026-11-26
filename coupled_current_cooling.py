#Here we will see how temperarure changes take place when h and i change simultaneously

import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
time_step = 1
total_time = 1200

time_values = np.arange(
    0, total_time + time_step, time_step
)

# Current profile
current_profile = np.zeros(len(time_values))

# Cooling coefficient profile
h_profile = np.zeros(len(time_values))

for i, t in enumerate(time_values):

    if t < 300:
        current_profile[i] = 2
        h_profile[i] = 10

    elif t < 600:
        current_profile[i] = 5
        h_profile[i] = 10

    elif t < 900:
        current_profile[i] = 5
        h_profile[i] = 30

    else:
        current_profile[i] = 3
        h_profile[i] = 30

# Battery properties
mass = 0.070
specific_heat = 1000
resistance = 0.025

ambient_temperature = 25
surface_area = 0.01
initial_temperature = 25
heat_generation_history = []
heat_loss_history = []
# Temperature simulation
temperature = initial_temperature
temperature_history = [temperature]

for i in range(1, len(time_values)):

    current = current_profile[i]
    h = h_profile[i]

    heat_generation = current**2 * resistance

    heat_loss = h * surface_area * (
        temperature - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    heat_generation_history.append(heat_generation)
    heat_loss_history.append(heat_loss)

    temperature_change = (
        net_heat * time_step
        / (mass * specific_heat)
    )

    temperature += temperature_change

    temperature_history.append(temperature)

# Plot temperature
plt.figure(figsize=(10, 5))

plt.plot(time_values, temperature_history)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Battery Temperature Under Changing Current and Cooling")

plt.grid(True)
plt.savefig("coupled_thermal_simulation.png", dpi=300)
plt.show()


plt.figure(figsize=(10, 5))

plt.plot(time_values[1:], heat_generation_history,
         label="Heat Generation")

plt.plot(time_values[1:], heat_loss_history,
         label="Heat Loss")

plt.xlabel("Time (seconds)")
plt.ylabel("Heat Rate (W)")
plt.title("Battery Heat Generation vs Heat Loss")

plt.legend()
plt.grid(True)
plt.show()