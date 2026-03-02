import random

def ecc_authenticate(num_devices):
    """
    ECC-based authentication success rate
    """
    success = 0
    scale_penalty = num_devices / 2500

    for _ in range(num_devices):
        failure_prob = 0.06 + scale_penalty
        if random.random() > failure_prob:
            success += 1

    return success / num_devices