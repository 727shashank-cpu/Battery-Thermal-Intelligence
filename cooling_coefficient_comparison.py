#here we will see how different values of h can effect temperatures
import numpy as np
import matplotlib.pyplot as plt
# Battery properties
mass = 0.070
specific_heat = 1000
resistance = 0.025
current = 5
# Environmental properties
ambient_temperature = 25
surface_area = 0.01
initial_temperature = 25

h_values = [5,10,20,25,30,50]
time_step=1
total_time = 10000
time_values = np.arange(0, total_time + time_step, time_step)
plt.figure(figsize=(10,6))
for h in h_values:

    temperature = initial_temperature
    temperature_history = [temperature]

    for t in time_values[1:]:

        heat_generation = current**2 * resistance

        heat_loss = h * surface_area * (temperature - ambient_temperature)

        net_heat = heat_generation - heat_loss

        temperature_change = (net_heat / (mass * specific_heat)) * time_step

        temperature = temperature + temperature_change

        temperature_history.append(temperature)
    
    plt.plot(time_values, temperature_history, label=f"h = {h}")

    print(f"h = {h} | Final Temperature = {temperature:.2f} °C")

plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Battery Temperature for Different Cooling Coefficients")
plt.legend()
plt.grid(True)
plt.savefig("cooling_coefficient_comparison.png", dpi=300)
plt.show()


print("\nTheoretical Steady-State Temperatures")

for h in h_values:

    steady_state_temperature = (
        ambient_temperature
        + (current**2 * resistance) / (h * surface_area)
    )

    print(f"h = {h} | T_ss = {steady_state_temperature:.2f} °C")



results = {}

for h in h_values:

    temperature = initial_temperature
    temperature_history = [temperature]

    for t in time_values[1:]:

        heat_generation = current**2 * resistance
        heat_loss = h * surface_area * (temperature - ambient_temperature)

        net_heat = heat_generation - heat_loss
        temperature_change = (net_heat / (mass * specific_heat)) * time_step

        temperature += temperature_change
        temperature_history.append(temperature)

    results[h] = temperature

print("\nSteady-State Error Analysis")

for h in h_values:

    theoretical = ambient_temperature + (current**2 * resistance) / (h * surface_area)
    simulated = results[h]

    error = abs(theoretical - simulated)
    percentage_error = error / theoretical * 100

    print(f"h = {h} | Theoretical = {theoretical:.3f} °C | "
          f"Simulated = {simulated:.3f} °C | Error = {percentage_error:.3f}%")