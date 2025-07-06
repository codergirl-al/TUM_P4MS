import statistics
import math

def analyze_readings(readings):
    if not readings:
        print("Input list of readings must not be empty.")
        return None

    mean = statistics.mean(readings)
    log_mean = math.log(mean) if mean > 0 else None

    if len(readings) == 1:
        stdev = 0.0
        normalized = [0.0]
    else:
        stdev = statistics.stdev(readings)
        if stdev == 0.0:
            normalized = [0.0 for _ in readings]
        else:
            normalized = [round((x - mean) / stdev, 3) for x in readings]

    return {
        "mean": mean,
        "std_dev": round(stdev, 3),
        "min": min(readings),
        "max": max(readings),
        "log_mean": round(log_mean, 3) if log_mean is not None else None,
        "normalized": normalized
    }