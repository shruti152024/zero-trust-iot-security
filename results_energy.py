import matplotlib.pyplot as plt
import random

random.seed(42)

nodes = [50, 100, 200, 300, 400, 500]

energy_token = []
energy_ecc = []
energy_proposed = []

for n in nodes:
    token = 0.8 + (n / 800) + random.uniform(-0.03, 0.03)
    ecc = token + 0.4 + random.uniform(-0.03, 0.03)
    proposed = ecc + 0.5 + random.uniform(-0.03, 0.03)

    energy_token.append(round(token, 2))
    energy_ecc.append(round(ecc, 2))
    energy_proposed.append(round(proposed, 2))

print("Devices | Token | ECC | ECC+ZT+IDS")
for i in range(len(nodes)):
    print(nodes[i], energy_token[i], energy_ecc[i], energy_proposed[i])

plt.figure(figsize=(7,4))
plt.plot(nodes, energy_token, '--s', label="Token-based")
plt.plot(nodes, energy_ecc, '-.o', label="ECC")
plt.plot(nodes, energy_proposed, '-^', linewidth=2,
         label="ECC + Zero Trust + IDS")

plt.xlabel("Number of IoT Devices")
plt.ylabel("Energy Consumption (J)")
plt.title("Energy Consumption vs Network Size")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()