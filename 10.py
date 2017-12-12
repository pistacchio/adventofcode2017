INPUT = range(256)
INPUT_LENGTHS = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
# INPUT = [0, 1, 2, 3, 4]
# INPUT_LENGTHS = [3, 4, 1, 5]

current_position = 0

def get_sublist(length):
    sublist = []
    cursor = current_position
    for i in range(length):
        cursor = cursor % len(INPUT)
        sublist.append(INPUT[cursor])
        cursor += 1
    return sublist

def merge_sublist(sublist):
    cursor = current_position
    for i in sublist:
        cursor = cursor % len(INPUT)
        INPUT[cursor] = i
        cursor += 1

for i, ln in enumerate(INPUT_LENGTHS):
    sublist = get_sublist(ln)
    sublist.reverse()
    merge_sublist(sublist)
    current_position = (current_position + ln + i) % len(INPUT)

print INPUT[0] * INPUT[1]