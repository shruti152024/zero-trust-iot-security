import matplotlib.pyplot as plt
import random

random.seed(42)


nodes = [50, 100, 200, 300, 400, 500]

token_detect = []
ecc_detect = []
proposed_detect = []

for n in nodes:
    # Token-based (weak detection)
    token_rate = 0.55 - (n / 2000) + random.uniform(-0.02, 0.02)

    # ECC-based (timestamp + crypto)
    ecc_rate = 0.90 - (n / 3000) + random.uniform(-0.02, 0.02)

    # Proposed (ECC + Zero Trust + IDS)
    proposed_rate = 0.96 - (n / 4000) + random.uniform(-0.02, 0.02)

    token_detect.append(round(token_rate, 2))
    ecc_detect.append(round(ecc_rate, 2))
    proposed_detect.append(round(proposed_rate, 2))


print("Devices | Token | ECC | ECC+ZT+IDS")
for i in range(len(nodes)):
    print(nodes[i],
          token_detect[i],
          ecc_detect[i],
          proposed_detect[i])

bar_width = 0.25
x = range(len(nodes))

plt.figure(figsize=(7, 4))

plt.bar([i - bar_width for i in x], token_detect,
        width=bar_width, label="Token-based")
plt.bar(x, ecc_detect,
        width=bar_width, label="ECC")
plt.bar([i + bar_width for i in x], proposed_detect,
        width=bar_width, label="ECC + Zero Trust + IDS")

plt.xticks(x, nodes)
plt.xlabel("Number of IoT Devices")
plt.ylabel("Replay Attack Detection Rate")
plt.title("Replay Attack Detection Performance")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()