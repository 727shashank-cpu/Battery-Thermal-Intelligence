# Battery Thermal Intelligence
# Experiment 02: Effect of Current on Heating

# Battery properties
resistance = 0.025
mass = 0.070
specific_heat = 1000
time = 600

# Different electrical currents
currents = [2, 4, 6, 8, 10]

print("CURRENT vs BATTERY HEATING")
print("--------------------------")

# Repeat calculations for each current
for current in currents:

    # Calculate heat generation
    heat_power = current**2 * resistance

    # Calculate total heat energy
    heat_energy = heat_power * time

    # Calculate temperature rise
    temperature_rise = heat_energy / (mass * specific_heat)

    # Display results
    print(f"Current: {current} A | "
          f"Power: {heat_power:.3f} W | "
          f"Temperature rise: {temperature_rise:.2f} K")