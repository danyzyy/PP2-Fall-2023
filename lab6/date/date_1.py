from datetime import datetime, timedelta

today = datetime.now()
fiv_day = today - timedelta(days=5)


print("Seichas", today.strftime("%Y-%m-%d"))
print("5 dnei nazad", fiv_day.strftime("%Y-%m-%d"))
