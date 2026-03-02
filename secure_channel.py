def calculate_latency(num_devices, mode):
    base = 5 + (num_devices / 200)

    if mode == "token":
        return base
    elif mode == "ecc":
        return base + 1.0
    else:  # proposed
        return base + 2.2