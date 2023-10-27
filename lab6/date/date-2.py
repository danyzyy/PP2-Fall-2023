from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("yesterday", yesterday)
print("today", today)
print("tomorrow", tomorrow)
