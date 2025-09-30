import time

duration = int(input('How long do you need to stay for?\n1 - Up to 2hrs\n2 - Up to 4 hours\n3 - Up to 12 hours\n> '))

localtime = time.time()
current = time.ctime(localtime)
twohrs = localtime + 7200
fourhrs = localtime + 14400
twelvehrs = localtime + 43200

if duration == 1:
    print(f'Current time: {current}\n\nExpires: {time.ctime(twohrs)}')
if duration == 2:
    print(f'Current time: {current}\n\nExpires: {time.ctime(fourhrs)}')
if duration == 3:
    print(f'Current time: {current}\n\nExpires: {time.ctime(twelvehrs)}')
