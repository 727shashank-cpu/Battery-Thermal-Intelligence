import matplotlib.pyplot as plt
import numpy as np
# Battery properties
mass = 0.070
specific_heat = 1000
resistance = 0.025

# Environmental properties
ambient_temperature = 25
h = 10
surface_area = 0.01
initial_temperature = 25

#different electrical currents
current_values = [1,2,3,4,5,6,7,8,9,10]


# Simulation settings
time_step = 1
total_time = 4000

time_values = np.arange(
    0, total_time + time_step, time_step
)

# Store temperature data for every current
temperature_history = {}

# Simulate each current
for current in current_values:

    temperature = initial_temperature
    temperature_values = [temperature]

    # Heat generation for this current
    heat_generation = current**2 * resistance

    # Time simulation
    for t in time_values[1:]:

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

    # Store results
    temperature_history[current] = temperature_values
for current in current_values:
    print(f"Current: {current} A | "
          f"Final Temperature: {temperature_history[current][-1]:.2f} °C")
# Extract steady-state temperatures
steady_temperatures = []

for current in current_values:
    steady_temperatures.append(
        temperature_history[current][-1]
    )

# Plot current vs steady-state temperature
plt.figure(figsize=(9, 5))

plt.plot(
    current_values,
    steady_temperatures,
    marker='o'
)

plt.xlabel("Current (A)")
plt.ylabel("Steady-State Temperature (°C)")
plt.title("Steady-State Temperature vs Current")

plt.grid(True)
plt.savefig("temperature_vs_current.png", dpi=300)
plt.show()

# Quadratic relationship analysis

current_squared = []
temperature_rise = []

for current in current_values:

    current_squared.append(current**2)

    rise = (
        temperature_history[current][-1]
        - ambient_temperature
    )

    temperature_rise.append(rise)


# Plot temperature rise vs current squared

plt.figure(figsize=(9, 5))

plt.plot(
    current_squared,
    temperature_rise,
    marker='o'
)

plt.xlabel("Current squared (A²)")
plt.ylabel("Temperature rise (°C)")
plt.title("Temperature Rise vs Current Squared")

plt.grid(True)
plt.savefig("temperature_rise_vs_current_squared.png", dpi=300)
plt.show()


# Temperature vs Time for different currents

plt.figure(figsize=(10, 6))

for current in current_values:

    plt.plot(
        time_values,
        temperature_history[current],
        label=f"{current} A"
    )

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Battery Temperature vs Time for Different Currents")

plt.legend(title="Current")
plt.grid(True)

plt.savefig("temperature_vs_time_different_currents.png", dpi=300)

plt.show()
