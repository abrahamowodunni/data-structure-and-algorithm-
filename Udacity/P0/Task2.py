"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longest_time_on_phone(calls):
    phone_times = {}

    for call in calls:
        phone1, phone2, date, duration = call
        duration_seconds = int(duration)

        # Update time for phone1
        phone_times[phone1] = phone_times.get(phone1, 0) + duration_seconds

        # Update time for phone2
        phone_times[phone2] = phone_times.get(phone2, 0) + duration_seconds

    # Find the telephone number with the longest time
    max_phone = max(phone_times, key=phone_times.get)
    max_time = phone_times[max_phone]

    return max_phone, max_time
    
max_phone, max_time = longest_time_on_phone(calls)
f"{max_phone} spent the longest time, {max_time} seconds, on the phone during September 2016."