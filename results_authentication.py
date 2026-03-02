import random
import matplotlib.pyplot as plt


random.seed(42)

def simulate_authentication(num_devices, mode="baseline"):
    """
    mode:
    - baseline : token only
    - ecc      : ECC authentication
    - proposed : ECC + Zero Trust + IDS
    """
    success = 0

    for _ in range(num_devices):
        scale_penalty = num_devices / 5000

        if mode == "baseline":
            failure_prob = 0.10 + scale_penalty
        elif mode == "ecc":
            failure_prob = 0.06 + scale_penalty
        else:  # proposed
            failure_prob = 0.03 + scale_penalty

        if random.random() > failure_prob:
            success += 1

    return success / num_devices


def average_authentication(num_devices, mode, runs=5):
    total = 0
    for _ in range(runs):
        total += simulate_authentication(num_devices, mode)
    return total / runs


nodes = [50, 100, 200, 300, 400, 500]

auth_baseline = []
auth_ecc = []
auth_proposed = []

for n in nodes:
    auth_baseline.append(average_authentication(n, "baseline"))
    auth_ecc.append(average_authentication(n, "ecc"))
    auth_proposed.append(average_authentication(n, "proposed"))


print("Devices | Token | ECC | ECC+ZT+IDS")
for i in range(len(nodes)):
    print(nodes[i],
          round(auth_baseline[i], 3),
          round(auth_ecc[i], 3),
          round(auth_proposed[i], 3))


plt.figure(figsize=(7, 4))
plt.plot(nodes, auth_baseline, '--o', label="Token-based")
plt.plot(nodes, auth_ecc, '-.o', label="ECC-based Authentication")
plt.plot(nodes, auth_proposed, '-o', linewidth=2,
         label="ECC + Zero Trust + IDS")

plt.ylim(0.75, 1.0)
plt.xlabel("Number of IoT Devices")
plt.ylabel("Authentication Success Rate")
plt.title("Authentication Performance Comparison (Averaged over 5 Runs)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()