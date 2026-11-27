
import numpy as np
import matplotlib.pyplot as plt

# =====================================
# 1. CELL SPECIFICATIONS
# =====================================

# NMC 18650
nmc_capacity = 2.5       # Ah
nmc_radius = 0.009       # m
nmc_height = 0.065       # m

# LFP 18650
lfp_capacity = 2.0       # Ah
lfp_radius = 0.009       # m
lfp_height = 0.065       # m


# =====================================
# 2. THERMAL PARAMETERS
# =====================================

# PROVISIONAL values - replace after verification
nmc_mass = 0.045         # kg
lfp_mass = 0.045         # kg

nmc_cp = 1000            # J/kg K
lfp_cp = 1000            # J/kg K

# Reference resistance at 30°C
# PROVISIONAL graph-read estimates
nmc_R_ref = 0.100        # ohm
lfp_R_ref = 0.062        # ohm

nmc_alpha = -0.0125      # 1/°C
lfp_alpha = -0.0323      # 1/°C

reference_temperature = 30  # °C


# =====================================
# 3. OPERATING CONDITIONS
# =====================================

C_rate = 1

ambient_temperature = 25
initial_temperature = 25

h = 20                   # W/m² K

time_step = 1
total_time = 5000

time_values = np.arange(
    0, total_time + time_step, time_step
)

# Current at 1C
nmc_current = C_rate * nmc_capacity
lfp_current = C_rate * lfp_capacity


# =====================================
# INITIAL HEAT GENERATION COMPARISON
# =====================================

nmc_initial_R = nmc_R_ref * (
    1 + nmc_alpha *
    (initial_temperature - reference_temperature)
)

lfp_initial_R = lfp_R_ref * (
    1 + lfp_alpha *
    (initial_temperature - reference_temperature)
)

nmc_initial_heat = nmc_current**2 * nmc_initial_R
lfp_initial_heat = lfp_current**2 * lfp_initial_R

print("NMC initial resistance:", nmc_initial_R)
print("LFP initial resistance:", lfp_initial_R)

print("NMC initial heat generation:", nmc_initial_heat)
print("LFP initial heat generation:", lfp_initial_heat)


# =====================================
# 4. SURFACE AREA
# =====================================

nmc_area = (
    2 * np.pi * nmc_radius * nmc_height
    + 2 * np.pi * nmc_radius**2
)

lfp_area = (
    2 * np.pi * lfp_radius * lfp_height
    + 2 * np.pi * lfp_radius**2
)

nmc_heat_history = []
lfp_heat_history = []

# =====================================
# 5. NMC SIMULATION
# =====================================

temperature_nmc = initial_temperature
nmc_history = [temperature_nmc]

for t in time_values[1:]:

    resistance = nmc_R_ref * (
        1 + nmc_alpha *
        (temperature_nmc - reference_temperature)
    )

    heat_generation = nmc_current**2 * resistance

    heat_loss = h * nmc_area * (
        temperature_nmc - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat / (nmc_mass * nmc_cp)
    ) * time_step

    temperature_nmc += temperature_change
    nmc_history.append(temperature_nmc)
    nmc_heat_history.append(heat_generation)


# =====================================
# 6. LFP SIMULATION
# =====================================

temperature_lfp = initial_temperature
lfp_history = [temperature_lfp]

for t in time_values[1:]:

    resistance = lfp_R_ref * (
        1 + lfp_alpha *
        (temperature_lfp - reference_temperature)
    )

    heat_generation = lfp_current**2 * resistance

    heat_loss = h * lfp_area * (
        temperature_lfp - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat / (lfp_mass * lfp_cp)
    ) * time_step

    temperature_lfp += temperature_change
    lfp_history.append(temperature_lfp)
    lfp_heat_history.append(heat_generation)


# =====================================
# 7. RESULTS
# =====================================

nmc_final = nmc_history[-1]
lfp_final = lfp_history[-1]

print("\nNMC final temperature:", nmc_final, "°C")
print("LFP final temperature:", lfp_final, "°C")

print("NMC temperature rise:", nmc_final - ambient_temperature)
print("LFP temperature rise:", lfp_final - ambient_temperature)


# =====================================
# 8. GRAPH
# =====================================

plt.figure(figsize=(10, 6))

plt.plot(
    time_values,
    nmc_history,
    label="NMC"
)

plt.plot(
    time_values,
    lfp_history,
    label="LFP"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Temperature (°C)")

plt.title("NMC vs LFP Thermal Comparison")

plt.legend()
plt.grid()

plt.savefig(
    "realistic_nmc_lfp_comparison.png",
    dpi=300
)

plt.show()



# =====================================
# HEAT GENERATION GRAPH
# =====================================

plt.figure(figsize=(10, 6))

plt.plot(
    time_values[1:],
    nmc_heat_history,
    label="NMC"
)

plt.plot(
    time_values[1:],
    lfp_heat_history,
    label="LFP"
)

plt.xlabel("Time (seconds)")
plt.ylabel("Heat Generation (W)")
plt.title("NMC vs LFP: Heat Generation vs Time")

plt.legend()
plt.grid()

plt.savefig("nmc_lfp_heat_generation.png", dpi=300)
plt.show()