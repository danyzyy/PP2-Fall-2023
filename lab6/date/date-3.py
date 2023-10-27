from datetime import datetime
now = datetime(2023, 10, 26, 15, 30, 45, 123456)
date_nomic = now.replace(microsecond=0)

print("datetime:", now)
print("Date without microseconds:", date_nomic)
