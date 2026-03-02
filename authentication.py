import random

def token_authenticate(num_devices):
    """
    Token-based authentication success rate
    """
    success = 0
    scale_penalty = num_devices / 2500

    for _ in range(num_devices):
        failure_prob = 0.10 + scale_penalty
        if random.random() > failure_prob:
            success += 1

    return success / num_devices