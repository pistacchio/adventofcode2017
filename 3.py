STARTING_LOCATION = 312051
TARGET_LOCATION   = 1

memory = {
    (0, 0): 1
}
current_loc_num = 1
current_loc     = (0, 0)
current_circle  = 0

def add_circle(circle_num, current_loc_num, current_loc):
    circle_steps = circle_num * 2
    # 1 east
    current_loc_num += 1
    current_loc = (current_loc[0] + 1, current_loc[1])
    memory[current_loc] = current_loc_num

    # circle_steps - 1 north
    for x in range(circle_steps - 1):
        current_loc_num += 1
        current_loc = (current_loc[0], current_loc[1]-1)
        memory[current_loc] = current_loc_num

    # circle_steps west
    for x in range(circle_steps):
        current_loc_num += 1
        current_loc = (current_loc[0]-1, current_loc[1])
        memory[current_loc] = current_loc_num

    # circle_steps south
    for x in range(circle_steps):
        current_loc_num += 1
        current_loc = (current_loc[0], current_loc[1]+1)
        memory[current_loc] = current_loc_num

    # circle_steps east
    for x in range(circle_steps):
        current_loc_num += 1
        current_loc = (current_loc[0]+1, current_loc[1])
        memory[current_loc] = current_loc_num

    return (current_loc_num, current_loc)

# construct the circular memory
while current_loc_num <= STARTING_LOCATION:
    current_circle += 1
    current_loc_num, current_loc = add_circle(current_circle, current_loc_num, current_loc)

current_loc = [k for k, v in memory.iteritems() if v == STARTING_LOCATION][0]
print abs(current_loc[0]) + abs(current_loc[1])
