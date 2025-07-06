from datetime import datetime

def compute_icu_stay_duration(admission_time: str, discharge_time: str) -> float:
    try:
        fmt = "%Y-%m-%d %H:%M:%S"
        admission_dt = datetime.strptime(admission_time, fmt)
        discharge_dt = datetime.strptime(discharge_time, fmt)

        if discharge_dt < admission_dt:
            print("Discharge time cannot be earlier than admission time.")
            return -1.0

        duration = (discharge_dt - admission_dt).total_seconds() / 3600
        return round(duration, 2)

    except ValueError as e:
        print(f"Invalid datetime format: {e}")
        return -1.0
