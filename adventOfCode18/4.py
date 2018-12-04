import re
from collections import defaultdict

f = open("4.txt", "r")

yo = []

for l in f:
    date, status = l.strip().split("]")
    [yeah, mounth, day, hour, min] = [x for x in re.findall("\d+", date)]
    yo.append([yeah + mounth + day + hour + min, yeah, mounth, day, hour, min, status.strip()])

yo = list(sorted(yo))
ids = defaultdict(lambda:0)

start_sleep = 0
current_guard = None
intervals = []
for l in yo:
    minute = l[5]
    status = l[-1]
    if re.findall("\d+", status) != []:
        guard = re.findall("\d+", status)[0]
        current_guard = guard
    if status == "falls asleep":
        start_sleep = int(minute)
    if status == "wakes up":
        ids[current_guard] += int(minute) - int(start_sleep)
        intervals.append([current_guard, int(start_sleep), int(minute)])


max_guard = max(ids.items(), key=lambda x: x[1])[0]


sleep_at_minutes = defaultdict(lambda:0)
for inv in intervals:
    if inv[0] == max_guard:
        for i in range(inv[1], inv[2]+1):
            sleep_at_minutes[i] += 1
max_minute = max(sleep_at_minutes.items(), key=lambda x: x[1])[0]

print("First:",  int(max_guard), int(max_minute), int(max_guard) * int(max_minute))

ids = ids.keys()
max_guard_minute = []
for g in ids:
    max_minute = 0
    sleep_at_minutes = defaultdict(lambda: 0)
    for inv in intervals:
        if inv[0] == g:
            for i in range(inv[1], inv[2] + 1):
                sleep_at_minutes[i] += 1
        max_minute = sleep_at_minutes[0]
        max_count = 0
        for m in sleep_at_minutes:
            if sleep_at_minutes[m] > sleep_at_minutes[max_minute]:
                max_minute = m
                max_count = sleep_at_minutes[m]
    max_guard_minute.append([g, max_minute, max_count])


best = max(max_guard_minute, key=lambda x: x[2])
print("Second:", int(best[0]), int(best[1]), int(best[0]) * int(best[1]))