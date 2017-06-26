

import random
final_count = 0

history = []


open_file = open("input.txt", "r")

value = open_file.readline()
input_value = []

for i in value:
    if i == "S" or i == "P" or i == "R":
        input_value.append(i)

# LOGIC
def bot(h):

    empty = True

    if len(h) <= 1:
        return random.choice("RSP")
    elif len(h) >= 2:
        for i in h:
            if i !=h[0]:
                empty = False
                break



    if empty == True:
        if h[0] == "R":
            return "P"
        elif h[0] == "S":
            return "R"
        elif h[0] == "P":
            return "S"
    else:
        return random.choice("RSP")





def get_score(player, comp):

    count = 0
    if player == comp:
        count += 0

    elif (player == "R" and comp == "S") or (player == "P" and comp == "R") or (player == "S" and comp == "P"):
        count += 1
    else:
        count -= 1
    return count


for i in input_value:
    history.append(i)
    bot_value = bot(history)
    final_count += get_score(i, bot_value)
print final_count


"""
def generate_same_shapes(n):
    same_shapes = []
    for i in range(0,len(input_value)):
        same_shapes.append(n)
    return same_shapes

count = 0
for i in generate_same_shapes("R"):
    count += get_score(i,bot())

print count
"""

