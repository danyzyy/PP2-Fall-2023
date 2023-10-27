from datetime import datetime

date1 = datetime(2023, 10, 26, 15, 30, 0)
date2 = datetime(2023, 10, 26, 16, 0, 0)
diff = date2 - date1
diffsec = diff.total_seconds()

print("first date:", date1)
print("second date:", date2)
print("Time difference in seconds:", diffsec)
