import numpy as np

"""
1) Open Door 1.
2) If Monty opens door 2: stay at Door 1
3) If Monty opens door 3: change Door 1 """


win, lose = 0, 0
Num = 10000
doors = list(("Door 1", "Door 2", "Door 3"))
present = doors[0]

for i in range(0, Num):
    door_select = doors[0]

#   Monty opens a door that is different from the contestant's selection
    Monty_opens = list(set(doors)-set([door_select, present]))
    if len(Monty_opens) == 2:
        Monty_opens = np.random.choice(Monty_opens, 1)
#    print(Monty_opens)

#   The door which is not the opened door nor the participant's selection
    Not_opened_door = list(set(doors)-set([door_select, Monty_opens[0]]))
#    print(Not_opened_door)

    if Monty_opens == doors[1]:
        # Staying at door 1 because Monty opens door 2
        door_select = present
        win += 1
    elif Monty_opens == doors[2]:
        # Changing door because Monty opens door 3
        door_select = doors[1]
        lose += 1

print("The probability of wining is: ", win/Num)
print("The probability of losing is: ", lose/Num)
