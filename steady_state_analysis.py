import matplotlib.pyplot as plt
#battery parameters
ambient_temp = 25.0        # Ambient temperature in degrees Celsius
current = 5.0             # Current in amperes (A)
resistance = 0.025        # Internal resistance in ohms (Ω)
surface_area = 0.01         # Surface area in square meters (m²)
#list containing different values of h
h_values = [1,2,3,4,5, 10, 20, 30, 50, 100]  # Heat transfer coefficients in W/(m² K)
def calculate_steady_state_temperature(ambient_temp, current, resistance, h, surface_area):
    """
    Calculate the steady-state temperature of the battery.

    Parameters:
    ambient_temp (float): Ambient temperature in degrees Celsius.
    current (float): Current in amperes (A).
    resistance (float): Internal resistance in ohms (Ω).
    h (float): Heat transfer coefficient in W/(m² K).
    surface_area (float): Surface area in square meters (m²).

    Returns:
    float: Steady-state temperature in degrees Celsius.
    """
    heat_generation = current**2 * resistance
    steady_state_temp = ambient_temp + heat_generation / (h * surface_area)
    return steady_state_temp
#calculations of equilibrium temperatures
steady_temperatures=[]
for h in h_values:
    steady_state_temp = calculate_steady_state_temperature(ambient_temp, current, resistance, h, surface_area)
    steady_temperatures.append(steady_state_temp)
    print(f"Steady-state temperature for h = {h} W/(m² K): {steady_state_temp:.2f} °C")

#plotting of the results
plt.plot(h_values, steady_temperatures, marker='o')
plt.xlabel("Heat Transfer Coefficient (h) [W/(m² K)]")
plt.ylabel("Steady-State Temperature (°C)")
plt.title("Steady-State Temperature vs Heat Transfer Coefficient")
plt.grid()
plt.savefig("steady_state_temperature.png", dpi=200)