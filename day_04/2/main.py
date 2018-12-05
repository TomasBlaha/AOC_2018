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
is_asleep = False
for time_record_object in time_record_objects:
    guard_search = re.search('\#([0-9]*)\s', time_record_object.event)
    if guard_search:
        current_guard = guard_search.group(1)
        last_minute = 0
        is_asleep = False
    else:
        if time_record_object.event == "wakes up":
            is_asleep = False
        else:
            is_asleep = True

        date = time_record_object.dt[0:10]
        if current_guard not in guards_records:
            guards_records.update({current_guard: {}})
        if date not in guards_records[current_guard]:
            guards_records[current_guard].update({date: {}})

        append = {}
        minute = int(time_record_object.dt[14:17])
        for i in range(last_minute, minute):
            append.update({i: is_asleep})

        guards_records[current_guard][date].update(append)
        last_minute = minute

maximum_minute = 0
maximum_minutes_count = 0
maximum_guard = 0
for guard, guard_record in guards_records.items():
    minutes = []
    for date, times in guard_record.items():
        for time, is_asleep in times.items():
            if not is_asleep:
                minutes.append(time)

    max_minute = max(set(minutes), key=minutes.count)
    max_minute_count = minutes.count(max_minute)

    if max_minute_count > maximum_minutes_count:
        maximum_minute = max_minute
        maximum_minutes_count = max_minute_count
        maximum_guard = guard

print(int(maximum_minute) * int(maximum_guard))
