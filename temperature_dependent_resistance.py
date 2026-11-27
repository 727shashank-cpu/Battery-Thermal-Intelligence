import numpy as np
import matplotlib.pyplot as plt

mass = 0.070
specific_heat = 1000

reference_resistance = 0.025
alpha = 0.004

reference_temperature = 25
ambient_temperature = 25
initial_temperature = 25

surface_area = 0.01
h = 10
current = 5

time_step = 1
total_time = 5000

time_values = np.arange(0, total_time + time_step, time_step)

temperature = initial_temperature

temperature_history = [temperature]
resistance_history = []

for t in time_values[1:]:

    resistance = reference_resistance * (
        1 + alpha * (temperature - reference_temperature)
    )

    heat_generation = current**2 * resistance

    heat_loss = h * surface_area * (
        temperature - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat / (mass * specific_heat)
    ) * time_step

    temperature += temperature_change

    temperature_history.append(temperature)
    resistance_history.append(resistance)

plt.figure(figsize=(10, 6))

plt.plot(time_values, temperature_history, label="Temperature-dependent resistance")

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Battery Temperature with Temperature-Dependent Resistance")

plt.legend()
plt.grid()

plt.savefig("temperature_dependent_resistance.png", dpi=300)
plt.show()


# Constant resistance model

constant_temperature = initial_temperature
constant_temperature_history = [constant_temperature]

for t in time_values[1:]:

    heat_generation = current**2 * reference_resistance

    heat_loss = h * surface_area * (
        constant_temperature - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat / (mass * specific_heat)
    ) * time_step

    constant_temperature += temperature_change

    constant_temperature_history.append(constant_temperature)


plt.figure(figsize=(10, 6))

plt.plot(
    time_values,
    constant_temperature_history,
    label="Constant Resistance"
)

plt.plot(
    time_values,
    temperature_history,
    label="Temperature-Dependent Resistance"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")
plt.title("Comparison of Battery Thermal Models")

plt.legend()
plt.grid()

plt.savefig("constant_vs_variable_resistance.png", dpi=300)
plt.show()