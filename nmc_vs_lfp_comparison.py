
import numpy as np
import matplotlib.pyplot as plt

# Common parameters
mass = 0.070
specific_heat = 1000
ambient_temperature = 25
initial_temperature = 25
surface_area = 0.01
h = 10
current = 5

time_step = 1
total_time = 5000

time_values = np.arange(
    0, total_time + time_step, time_step
)

# NMC parameters
R_nmc = 0.100
alpha_nmc = -0.0125

# LFP parameters
R_lfp = 0.062
alpha_lfp = -0.0323

reference_temperature = 30

# NMC simulation
temperature_nmc = initial_temperature
nmc_history = [temperature_nmc]

for t in time_values[1:]:

    resistance = R_nmc * (
        1 + alpha_nmc *
        (temperature_nmc - reference_temperature)
    )

    heat_generation = current**2 * resistance

    heat_loss = h * surface_area * (
        temperature_nmc - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat / (mass * specific_heat)
    ) * time_step

    temperature_nmc += temperature_change
    nmc_history.append(temperature_nmc)


# LFP simulation
temperature_lfp = initial_temperature
lfp_history = [temperature_lfp]

for t in time_values[1:]:

    resistance = R_lfp * (
        1 + alpha_lfp *
        (temperature_lfp - reference_temperature)
    )

    heat_generation = current**2 * resistance

    heat_loss = h * surface_area * (
        temperature_lfp - ambient_temperature
    )

    net_heat = heat_generation - heat_loss

    temperature_change = (
        net_heat / (mass * specific_heat)
    ) * time_step

    temperature_lfp += temperature_change
    lfp_history.append(temperature_lfp)


# Plot comparison
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
plt.title("NMC vs LFP: Battery Thermal Comparison")

plt.legend()
plt.grid()

plt.savefig("nmc_vs_lfp_comparison.png", dpi=300)
plt.show()

nmc_rise = nmc_history[-1] - ambient_temperature
lfp_rise = lfp_history[-1] - ambient_temperature

percentage_reduction = (
    (nmc_rise - lfp_rise) / nmc_rise
) * 100

print("NMC Temperature Rise:", nmc_rise)
print("LFP Temperature Rise:", lfp_rise)
print("Reduction in Temperature Rise:", percentage_reduction, "%")