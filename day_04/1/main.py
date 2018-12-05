import re


class TimeRecord:
    def __init__(self, dt, event):
        self.dt = dt
        self.event = event


time_records = open("./1.input", "r").read().splitlines()
time_record_objects = []

for time_record in time_records:
    split_record = re.split('\[|\] ', time_record)
    time = split_record[1]
    time_record_objects.append(TimeRecord(time, split_record[2]))
time_record_objects.sort(key=lambda x: x.dt, reverse=False)

guards_records = {}
current_guard = None
last_minute = 0
current_guard_status = 1
for time_record_object in time_record_objects:
    guard_search = re.search('\#([0-9]*)\s', time_record_object.event)
    if guard_search:
        current_guard = guard_search.group(1)
        last_minute = 0
        current_guard_status = 1
    else:
        if time_record_object.event == "wakes up":
            current_guard_status = 1
        else:
            current_guard_status = 0

        date = time_record_object.dt[0:10]
        if current_guard not in guards_records:
            guards_records.update({current_guard: {}})
        if date not in guards_records[current_guard]:
            guards_records[current_guard].update({date: {}})

        append = {}
        minute = int(time_record_object.dt[14:17])
        for i in range(last_minute, minute):
            append.update({i: current_guard_status})

        guards_records[current_guard][date].update(append)
        last_minute = minute


maximum = 0
maximum_guard = None
maximum_minutes = []
for guard, guard_record in guards_records.items():
    count = 0
    minutes = []
    for date, times in guard_record.items():
        print(times.items())
        for time, status in times.items():
            if status == 1:
                count += 1
                minutes.append(time)
    if count > maximum:
        maximum = count
        maximum_guard = guard
        maximum_minutes = minutes

max_minute = max(set(maximum_minutes), key=maximum_minutes.count)
print(int(max_minute) * int(maximum_guard))