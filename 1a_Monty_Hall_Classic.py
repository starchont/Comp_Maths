import numpy as np

x, y = 0, 0
doors = list(("Door 1", "Door 2", "Door 3"))

# put the present at door 1
present = doors[0]

# Starting monte carlo simulation
for i in range(0, 10000):
    ran_num = np.random.rand(1)
    if ran_num < float(1/3):
        door_select = doors[0]
    elif float(1/3) <= ran_num <= float(2/3):
        door_select = doors[1]
    else:
        door_select = doors[2]

    # Monty opens a door without present
    Monty_opens = list(set(doors)-set([door_select, present]))

    # if door selected is the one with the present, Monty chooses to open a random door
    if len(Monty_opens) == 2:
        Monty_opens = np.random.choice(Monty_opens, 1)
    Not_opened_door = list(set(doors)-set([door_select, Monty_opens[0]]))

    # Not changing the selected door
    if door_select == present:
        x += 1

    # Always changing the selected door
    if Not_opened_door[0] == present:
        y += 1

print("the probability of wining by not changing door is : ", x/10000)
print("The probability of wining by changing the door is : ", y/10000)
