# Battery Thermal Intelligence
# Experiment 01: Understanding Joule Heating

# 1. Battery parameters
current = 5.0             # Current in amperes (A)
resistance = 0.025        # Internal resistance in ohms (Ω)

# 2. Thermal properties
mass = 0.070              # Battery mass in kg
specific_heat = 1000      # Specific heat capacity in J/(kg K)

# 3. Operating duration
time = 600                # Time in seconds

# 4. Calculate heat generation
heat_power = current**2 * resistance

# 5. Calculate total heat generated
heat_energy = heat_power * time

# 6. Calculate temperature rise (assuming no cooling)
temperature_rise = heat_energy / (mass * specific_heat)

# 7. Display results
print("BATTERY THERMAL EXPERIMENT")
print("--------------------------")
print(f"Heat generation rate: {heat_power:.3f} W")
print(f"Total heat generated: {heat_energy:.2f} J")
print(f"Temperature rise: {temperature_rise:.2f} K")