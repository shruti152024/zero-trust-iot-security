import matplotlib.pyplot as plt
import random

random.seed(42)

nodes = [50, 100, 200, 300, 400, 500]

latency_token = []
latency_ecc = []
latency_proposed = []


for n in nodes:
    # Token-based (lowest overhead)
    token_latency = 5 + (n / 100) + random.uniform(-0.05, 0.05)

    # ECC-based (cryptographic overhead)
    ecc_latency = token_latency + 1.0 + random.uniform(-0.05, 0.05)

    # Proposed: ECC + Zero Trust + IDS (highest)
    proposed_latency = ecc_latency + 1.2 + random.uniform(-0.05, 0.05)

    latency_token.append(round(token_latency, 2))
    latency_ecc.append(round(ecc_latency, 2))
    latency_proposed.append(round(proposed_latency, 2))

print("Devices | Token(ms) | ECC(ms) | ECC+ZT+IDS(ms)")
for i in range(len(nodes)):
    print(nodes[i],
          latency_token[i],
          latency_ecc[i],
          latency_proposed[i])

plt.figure(figsize=(7, 4))

plt.plot(nodes, latency_token, '--s', label="Token-based")
plt.plot(nodes, latency_ecc, '-.o', label="ECC")
plt.plot(nodes, latency_proposed, '-^', linewidth=2,
         label="ECC + Zero Trust + IDS")

plt.xlabel("Number of IoT Devices")
plt.ylabel("Average Latency (ms)")
plt.title("Latency Overhead vs Network Size")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()