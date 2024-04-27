"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def countNumber(texts,calls):
    empty = []
    for text,call in zip(texts,calls):
        empty.extend([text[0], text[1], call[0], call[1]])

    return len(set(empty))

count = countNumber(texts,calls)
print(f"There are {count} different telephone numbers in the records.")