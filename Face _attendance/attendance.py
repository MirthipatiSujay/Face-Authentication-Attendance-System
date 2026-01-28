import pandas as pd
import os
from datetime import datetime

ATTENDANCE_FILE = "data/attendance.csv"


def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not os.path.exists(ATTENDANCE_FILE):
        df = pd.DataFrame(columns=["Name", "Date", "PunchIn", "PunchOut"])
    else:
        df = pd.read_csv(ATTENDANCE_FILE)

    record = df[(df["Name"] == name) & (df["Date"] == date)]

    if record.empty:
        # Punch In
        df.loc[len(df)] = [name, date, time, ""]
        status = "Punch-In"
    else:
        # Punch Out (overwrite last)
        idx = record.index[-1]
        df.at[idx, "PunchOut"] = time
        status = "Punch-Out"

    df.to_csv(ATTENDANCE_FILE, index=False)
    return status
